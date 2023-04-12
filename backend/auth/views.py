from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from api.serializers import UserSerializer


class UserRegister(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)

        # TODO: Use huey for this
        send_mail(
            "Confirm your email address",
            "This will hopefully be url.",
            None,
            recipient_list=[serializer.validated_data.get("email")],
        )
