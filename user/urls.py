# write your code here
from django.contrib.auth.views import LoginView
from django.urls import path
from rest_framework.authtoken import views

from user.views import CreateUserView, LoginUserView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("manage/", ManageUserView.as_view(), name="manage"),
]

app_name = "auth"
