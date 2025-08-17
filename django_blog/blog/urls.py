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
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    
    path('post/<int:pk>/comment/', views.add_comment, name='add-comment'),

    path('tag/<int:tag_id>/', views.posts_by_tag, name='posts-by-tag'),
    path('search/', views.search_posts, name='search-posts'),


]