from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

# Simple list view (task 1)
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # inherits default permission: read-only for unauthenticated (per settings)

# Full CRUD with ViewSet (task 2)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # example: only authenticated users can modify; anyone can read
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# OPTIONAL 
# OPTIONAL 
# OPTIONAL 
# OPTIONAL 

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        user = token.user
        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username,
        })
