from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import CustomUser
from users.serializers import CustomUserSerializer


# Create your views here.
class RegisterAPIView(APIView):

    def post(self, request):

        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user=CustomUser(
                phone=serializer.validated_data['phone'],
                password=make_password(serializer.validated_data['password']),
            )
            user.save()
            token,created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "message":"User registered successfully",
                    "token":token.key,

                },
                status=status.HTTP_201_CREATED
            )

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(APIView):
    def post(self, request):
        print(request.data)
        phone= request.data.get('phone')
        password= request.data.get('password')

        user= authenticate(phone=phone,password=password)
        if user:
            token,created= Token.objects.get_or_create(user=user)
            return Response(
                {
                    "message":"User logged in",
                    "token":token.key,

                },
                status=status.HTTP_200_OK

            )

        else:
            return Response(
                {
                    "message":"User does not exist",
                }
            )



class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            user =request.user.auth_token.delete()
            return Response(
                {
                    "message":"User logged out",

                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message":str(e)

                },
                status=status.HTTP_400_BAD_REQUEST
            )





#
# class ForgotPasswordAPIView(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         form = PasswordResetForm(data={"email": email})
#         if form.is_valid():
#             form.save(request=request)  # This will send an email to the user
#             return Response({"message": "Password reset link sent."}, status=status.HTTP_200_OK)
#         return Response({"error": "Invalid email address"}, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import get_user_model
User = get_user_model()
class VerifyTokenView(APIView):
    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(auth_token=token)
            return Response({"message": "Token is valid", "user": user.username}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)

