from django.urls import path
from . import views

urlpatterns = [
    path('user', views.CustomUserList.as_view()),
    path('user/<int:pk>', views.CustomUserDetail.as_view()),
]