from rest_framework.response import Response
from rest_framework.views import APIView
from .models import HeaderImage, Services, Testimonial, ContactUs
from .serializers import HeaderImageSerializer, ServicesSerializer, TestimonailSerializer, UserSerializer, ContactSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import generics
from django.contrib.auth.decorators import login_required

# Create your views here.
class UserCreate(generics.CreateAPIView):
    
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class HeaderImageViewSet(viewsets.ModelViewSet):
    queryset = HeaderImage.objects.all()
    serializer_class = HeaderImageSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    
class TestimonailViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonailSerializer

class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer