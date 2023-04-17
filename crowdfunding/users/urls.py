from django.urls import path

from . import views

# from this directory import ALL Views and not one by one

urlpatterns = [
    path('', views.CustomUserList.as_view(), name='customuser-list'),
    # url / user / user id number
    path('<int:pk>/', views.CustomUserDetail.as_view(),
         name='customuser-detail-update'),
    path('session/', views.CustomUserSessionView.as_view(),
         name='customuser-session-view'),
    # path('register', views.CustomUserRegisterAPIView.as_view(),
    #      name='customuser-register')

]
