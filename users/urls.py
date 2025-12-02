from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, LoginView, LogoutView

app_name = "users"

urlpatterns = [
    # JWT API (기존)
    path("register/", RegisterView.as_view(), name="register_api"),
    path("login/", LoginView.as_view(), name="login_api"),
    path("logout/", LogoutView.as_view(), name="logout_api"),

    # HTML 로그인/로그아웃
    path("login/html/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/html/", auth_views.LogoutView.as_view(), name="logout"),
]
