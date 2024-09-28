from django.urls import path
from .views import UserView, LoginView

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
]
