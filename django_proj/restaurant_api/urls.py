from django.urls import path, include
from rest_framework import routers

from .views import RestaurantViewSet

router = routers.DefaultRouter()
router.register(
    "restaurant", RestaurantViewSet, basename="restaurant"
)

urlpatterns = [
    path("", include(router.urls)),
]