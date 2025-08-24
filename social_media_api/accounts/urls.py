from django.urls import path
from .views import AccountViewSet


account_list = AccountViewSet.as_view({
    "post": "register", # /register
})


urlpatterns = [
    path("register/", AccountViewSet.as_view({"post": "register"}), name="register"),
    path("login/", AccountViewSet.as_view({"post": "login"}), name="login"),
    path("profile/", AccountViewSet.as_view({"get": "profile", "patch": "profile"}), name="profile"),


    path("follow/<int:pk>/", AccountViewSet.as_view({"post": "follow"}), name="follow"),
    path("unfollow/<int:pk>/", AccountViewSet.as_view({"post": "unfollow"}), name="unfollow"),
]