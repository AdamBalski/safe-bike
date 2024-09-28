from django.urls import path
from .views import (
    ListRoutesView,
    RateView,
    ListDangerCategoriesView,
    CreateRouteView,
)

urlpatterns = [
    path("routes/", ListRoutesView.as_view(), name="routes"),
    path("route/<int:route_id>/score/", RateView.as_view(), name="score"),
    path(
        "danger-categories/",
        ListDangerCategoriesView.as_view(),
        name="danger-categories",
    ),
    path("route/", CreateRouteView.as_view(), name="create-route"),
]
