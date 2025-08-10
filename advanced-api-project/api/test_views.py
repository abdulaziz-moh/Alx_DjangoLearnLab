from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.author = Author.objects.create(name="Author One")
        self.book = Book.objects.create(title="Book One", publication_year=2020, author=self.author)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data[0])  # This ensures response.data is accessed

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        url = reverse('book-create')
        data = {"title": "New Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {"title": "New Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
