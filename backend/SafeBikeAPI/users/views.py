from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.
class UserView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        user = User.objects.get(username=request.data["username"])
        serializer = UserSerializer(user)
        return Response(serializer.data)
