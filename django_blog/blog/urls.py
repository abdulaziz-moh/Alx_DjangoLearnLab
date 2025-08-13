from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view, name = 'login'),
    path('logout/',views.logout_view, name = 'logout'),
    path('profile/',views.profile_view, name = 'profile'),
    path('register/',views.register_view, name = 'register'),
    path('posts/',views.base_view, name = 'posts'),
    path('',views.base_view, name = 'home'),
    
]