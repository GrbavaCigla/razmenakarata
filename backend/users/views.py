import json
import requests

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.views import APIView


class UserActivation(APIView):
    def get(self, request, uid, token):
        payload = {"uid": uid, "token": token}

        url = request.build_absolute_uri("/api/v1/users/activation/")
        response = requests.post(url, data=payload)

        if response.ok:
            return redirect(settings.ACTIVATION_REDIRECT)

        return JsonResponse(json.loads(response.content.decode()))
