from django.urls import path
from .views import ListRoutesView, RateView

urlpatterns = [
    path("routes/", ListRoutesView.as_view(), name="routes"),
    path("route/<int:route_id>/score/", RateView.as_view(), name="score"),
]
