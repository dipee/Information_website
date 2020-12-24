from django import urls
from django.urls import path, include
from .views import HeaderImageViewSet, ServicesViewSet, TestimonailViewSet, ContactViewSet
from API.views import UserCreate, LoginView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'header', HeaderImageViewSet)
router.register(r'services', ServicesViewSet)
router.register(r'testimonial', TestimonailViewSet)
router.register(r'contact', ContactViewSet)


urlpatterns = [
     path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]
urlpatterns += router.urls
