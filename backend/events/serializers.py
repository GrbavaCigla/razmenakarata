from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SlugRelatedField,
)

from .models import Event, Package, Ticket


class PackageSerializer(ModelSerializer):
    class Meta:
        model = Package
        exclude = ("event",)


class EventSerializer(ModelSerializer):
    thumbnail = HyperlinkedIdentityField(view_name="event-thumbnail")
    categories = SlugRelatedField(many=True, slug_field="name", read_only=True)
    packages = PackageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        exclude = ("created", "page")
        read_only_fields = ("categories", "packages")


class TicketSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="email", read_only=True)

    def to_representation(self, instance):
        self.fields["package"] = SlugRelatedField(slug_field="name", read_only=True)
        return super().to_representation(instance)

    class Meta:
        model = Ticket
        exclude = ("created", "event")
        read_only_fields = ("owner",)
