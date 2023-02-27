from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .filters import DynamicSearchFilter
from .models import Project, Pledge, Comment, Category
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly, IsCommenterOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.filters import OrderingFilter, SearchFilter
from .serializers import ProjectSerializer, ProjectDetailSerializer, PledgeSerializer, PledgeDetailSerializer,  CommentSerializer, CategorySerializer, CategoryDetailSerializer
from rest_framework.settings import api_settings

'''PROJECT LIST VIEW FOR PROJECTS & IF LOGGED IN YOU CAN ADD / DELETE PROJECTS'''


class ProjectList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'owner', 'date_created']

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id=None):
        project = self.get_object(id=id)
        serializer = ProjectDetailSerializer(project)
        project.delete()
        return Response(ProjectDetailSerializer.data, status=status.HTTP_204_NO_CONTENT)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(Project=self.request.user)


'''Pledge Create Only - NO EDITS / COMMENTS CAN NOT BE DELETED UNLESS USER IS DELETED'''
'''Logged in users are able to view & add pledges. Not logged in, view only'''


class PledgeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['supporter', 'project', 'anonymous']

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)


class PledgeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]
    permission_classes = []
    queryset = Pledge.objects.all()
    serializer_class = PledgeDetailSerializer

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        data = request.data
        serializer = PledgeSerializer(
            instance=pledge,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()


'''Comment Create Only - NO EDITS / COMMENTS CAN NOT BE DELETED UNLESS USER IS DELETED'''
'''Logged in users are able to view & add comments. Not logged in, view only'''


class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project',]

    def perform_create(self, serializer):
        serializer.save(commentator=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_object(self, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            self.check_object_permissions(self.request, comment)
            return comment
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        data = request.data
        serializer = CommentSerializer(
            instance=comment,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()


class CategoryList(generics.ListAPIView):
    """ url: categories/ """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    """ url: categories/<str:name>/"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'name'


'''BELOW TO CULL AS THEY DO NOT SEEM TO SERVE A PURPOSE'''


####################################################################################
# PAGEINATOR TO BE IMPLEMENTED
# class ProjectList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request):
#         projects = Project.objects.all()

#         #filter for open projects only
#         is_open = request.query_params.get('is_open', None)
#         if is_open:
#             projects = projects.filter(is_open=is_open)

#         #order by date created
#         order_by = request.query_params.get('order_by', None)
#         if order_by == 'date_created':
#             projects = projects.order_by(order_by)

#         #order by the most recent pledges
#         if order_by == 'recent_pledges':
#             projects = Project.objects.annotate(
#                 pledge_date=Max('pledges_date_created')
#             ).order_by(
#                 '-pledge_date'
#             )

#         #order by the number of pledges
#         if order_by == 'num_pledges':
#             projects = Project.objects.annotate(
#                 pledge_count=Count('pledges')
#             ).order_by(
#                 '-pledge_count'
#             )

#         paginator = LimitOffsetPagination()
#         result_page = paginator.paginate_queryset(projects, request)

#         serializer = ProjectSerializer(result_page, many=True)
#         return Response(serializer.data)
