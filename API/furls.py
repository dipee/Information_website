from django import urls
from API.views import UserCreate, LoginView
from django.urls import path, include
urlpatterns = [
     path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]
