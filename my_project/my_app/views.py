from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers.userSerializer import UserSerializer
from .serializers.personSerializer import PersonSerializer
from .models import Person
from django.contrib.auth.models import User


class SignUpView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        print(f'request.data: {request.data}')
        username = request.data.get('username')
        password = request.data.get('password')
        print(f'username: {username}, password: {password}')
        # user = authenticate(username=username, password=password)
        user = User.objects.get(username=username, password=password)
        if user:
            return Response({"token": Token.objects.get(user=user).key})
        else:
            return Response({"error": "Wrong Credentials"}, status=400)

