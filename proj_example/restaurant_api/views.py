from rest_framework import viewsets

from .serializers import RestaurantSerializer
from restaurant.models import Restaurant


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
