from django.urls import path
from .views import ListRoutesView

urlpatterns = [
    path("routes/", ListRoutesView.as_view(), name="routes"),
]
