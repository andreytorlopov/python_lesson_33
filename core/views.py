from typing import Any

from django.contrib.auth import login
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from core.serializers import CoreSerializer, LoginSerializer


class UserCreateView(CreateAPIView):
    serializer_class = CoreSerializer
    permission_classes = [AllowAny]


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        login(request, user=serializer.save())
        return Response(serializer.data)
