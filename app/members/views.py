from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_auth.registration.views import SocialLoginView
from rest_auth.serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client


class TestJWTView(APIView):
    def post(self, request):
        return Response({'user': request.user.username}, status=200)


def test_google_view(request):
    return HttpResponse(f'<p>{dict(request.GET)}<p>')

def test_google_token_view(request):
    return HttpResponse(f'<p>{dict(request.GET)}<p>')