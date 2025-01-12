from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'created_at', 'updated_at']
    fields = ['name', 'phone']

admin.site.register(Restaurant, RestaurantAdmin)