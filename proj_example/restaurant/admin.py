from django.contrib import admin
from .models import (
    Restaurant,
    RestaurantCategory,
    RestaurantStatistics,
    Keyword,
)


@admin.action(description="선택된 가게의 별점 초기화")
def reset_rating(modeladmin, request, queryset):
    queryset.update(rating=0.0, rating_count=0)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "category",
        "phone",
        "rating",
        "rating_count",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["id", "name"]
    list_filter = ["rating", "category"]
    search_fields = ["name", "phone"]
    ordering = ["-id"]
    actions = [reset_rating]
    autocomplete_fields = ["keywords"]


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]


admin.site.register(RestaurantCategory)

admin.site.register(RestaurantStatistics)
