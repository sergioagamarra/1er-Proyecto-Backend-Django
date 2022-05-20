from django.urls import path

#from .views import posts,home,post,create_post,edit_post, delete_post

from . import views

app_name = "auth"
urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
]