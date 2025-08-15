from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='home'), name = 'logout'),
    path('register/',views.register, name = 'register'),
    path('profile/',views.profile, name = 'profile'),
    
    
    path('posts/',views.base_view, name = 'posts'),
    path('',views.base_view, name = 'home'),
    
]