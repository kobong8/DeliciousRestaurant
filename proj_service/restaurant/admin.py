from django.contrib import admin

from .models import Article, Restaurant


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "show_at_index",
        "is_published",
        "created_at",
        "modified_at",
    ]
    fields = ["title", "preview_image", "content", "show_at_index", "is_published"]
    search_fields = ["title"]
    list_filter = ["show_at_index", "is_published"]
    date_hierarchy = "created_at"
    actions = ["make_published"]


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "branch_name",
        "is_closed",
        "phone",
        "rating",
        "rating_count",
    ]
    fields = [
        "name",
        "branch_name",
        "category",
        "is_closed",
        "phone",
        "latitude",
        "longitude",
        "tags",
    ]
    readonly_fields = ["rating", "rating_count"]
    search_fields = ["name", "branch_name"]
    list_filter = ["tags"]
    autocomplete_fields = ["tags"]
