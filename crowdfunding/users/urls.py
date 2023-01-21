from django.urls import path
from . import views
# from this directory import ALL Views and not one by one

urlpatterns = [
    path('', views.CustomUserList.as_view(), name='customuser-list'),
    path('<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),
]
