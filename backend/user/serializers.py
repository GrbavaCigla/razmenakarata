from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "email",
            "email_confirmed",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                # TODO: Make this invisible to the public
                "write_only": True,
                "allow_null": False,
                "required": True,
                "allow_blank": False,
            },
            "first_name": {
                "allow_null": False,
                "required": True,
                "allow_blank": False,
            },
            "last_name": {
                "allow_null": False,
                "required": True,
                "allow_blank": False,
            },
            "email_confirmed": {"read_only": True},
            "id": {"read_only": True},
        }
