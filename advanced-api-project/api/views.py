from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

    filter_backends = [
        filters.DjangoFilterBackend,
        drf_filters.SearchFilter,
        drf_filters.OrderingFilter
    ]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.AllowAny]
    
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['title', 'author__name', 'publication_year']
#     search_fields = ['title', 'author__name']
#     ordering_fields = ['title', 'publication_year']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
