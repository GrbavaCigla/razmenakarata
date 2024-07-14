import requests
import json

from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import redirect

from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView, Response

from .models import User
from .serializers import UserSerializer


class UserActivation(APIView):
    def get(self, request, uid, token):
        payload = {"uid": uid, "token": token}

        url = request.build_absolute_uri("/api/v1/users/activation/")
        response = requests.post(url, data=payload)

        if response.ok:
            return redirect(settings.ACTIVATION_REDIRECT)

        return JsonResponse(json.loads(response.content.decode()))


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
