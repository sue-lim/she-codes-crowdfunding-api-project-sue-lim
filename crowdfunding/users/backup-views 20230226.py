from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from .models import CustomUser
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions, generics
from .serializers import CustomUserSerializer, CustomUserDetailSerializer
from projects.permissions import IsOwnProfile

'''VIEW ALL USERS & CREATE USER'''


class CustomUserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'first_name', 'last_name']

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(users=self.request.user)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


'''VIEW USER & UPDATE DETAILS | RetrieveUpdateAPIView for single instances '''


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnProfile]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer

    # def get_object(self, pk):
    #     try:
    #         return CustomUser.objects.get(pk=pk)
    #     except CustomUser.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):
    #     user = self.get_object(pk)
    #     serializer = CustomUserSerializer(user)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     user = self.get_object(pk)
    #     data = request.data
    #     serializer = CustomUserSerializer(
    #         instance=user,
    #         data=data,
    #         partial=True
    #     )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response(
                {"data": "Sorry, user here!"}, status=status.HTTP_404_NOT_FOUND
            )
        return super(CustomUserDetail, self).handle_exception(exc)


'''ADD DEF DELETE FUNCTION'''

''' CLASS FOR SESSION VIEW '''


class CustomUserSessionView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    serializer_class = CustomUserDetailSerializer

    def get_object(self):
        return self.request.user

    # https://www.cdrf.co/3.13/rest_framework.generics/RetrieveUpdateDestroyAPIView.html


'''Class based view to Get User Details using Token Authentication'''


# class CustomUserDetailAPI(APIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (AllowAny,)

#     def get(self, request, *args, **kwargs):
#         user = CustomUser.objects.get(id=request.user.id)
#         serializer = CustomUserSerializer(user)
#         return Response(serializer.data)
