from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='home'), name = 'logout'),
    path('register/',views.register, name = 'register'),
    path('profile/',views.profile, name = 'profile'),
    
    
    # Home
    path('', views.PostListView.as_view(), name='home'),

    # Post CRUD
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    
]