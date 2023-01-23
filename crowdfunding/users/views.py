from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer, CustomUserRegisterSerializer
from rest_framework.authentication import TokenAuthentication


class CustomUserList(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CustomUserDetail(APIView):

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


# Class based view to Get User Details using Token Authentication
class CustomUserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


# Class based view to register user


class CustomUserRegisterAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CustomUserRegisterSerializer
