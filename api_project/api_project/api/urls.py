from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet, CustomObtainAuthToken

router = DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")

urlpatterns = [
    # simple list endpoint
    path("books/", BookList.as_view(), name="book-list"),
    # full CRUD via router
    path("", include(router.urls)),
    # token retrieval
    path("api-token-auth/", CustomObtainAuthToken.as_view(), name="api_token_auth"),
]
