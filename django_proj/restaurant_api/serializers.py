from rest_framework import serializers

# TODO restaurant path check required
from ..restaurant.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "category", "phone", "latitude", "longitude", "rating", "rating_count"]
