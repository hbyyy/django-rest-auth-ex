from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.shortcuts import render

# Create your views here.
from rest_auth.registration.views import SocialLoginView
from rest_auth.serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client


class TestView(APIView):
    def post(self, request):
        return Response({'user': request.user.username}, status=200)
