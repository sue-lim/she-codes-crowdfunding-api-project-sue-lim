from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('pledges/', views.PledgeList.as_view(), name='pledge-list'),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view(), name='pledge-detail'),
    path('comments/', views.CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('categories/', views.CategoryList.as_view()),
    path('category/<str:name>/', views.CategoryDetail.as_view()),
]
