from urllib import request
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer, CreateNewPasswordSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework.permissions import AllowAny
from .permissions import IsActive
from .utils import send_activation_code



class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Поздравляем! Вы зарегистрированы, код активации аккаунта отправлен на вашу почту.', 201
            )


class ActivationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, code, email):
        user = User.objects.get(
            email=email, activation_code=code
        )
        msg = (
            'Пользователь не найден',
            'Аккаунт активирован'
        )
        if not user:
            return Response(msg[0], 400)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response(msg[-1], 200)


class LogoutView(APIView):
    # permission_classes = [IsActive]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(token=refresh_token)
            token.blacklist()
            return Response('Вы обновили токен')
        except Exception as e:
            return Response('Вы вышли из аккаунта')


class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, email):
        user = get_object_or_404(User, email=email)
        user.is_active = False
        user.create_activation_code()
        user.save()
        send_activation_code(
            email=user.email, code=user.activation_code, 
            status='forgot_password'
        )
        return Response('Проверьте электронную почту', status=200)


class CompleteResetPasswordView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CreateNewPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Вы успешно сменили пароль', status=200
            )
