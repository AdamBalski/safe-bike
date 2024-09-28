from django.contrib import admin
from .models import Route, Segment, Score, DangerCategory


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("name", "owner_id", "id")
    search_fields = ("name",)
    filter_horizontal = ("segments",)


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    list_display = ("src_x", "src_y", "dest_x", "dest_y", "id")
    search_fields = ("src_x", "src_y", "dest_x", "dest_y")


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = (
        "owner_id",
        "segment_id",
        "danger_category_id",
        "score",
        "id",
    )
    search_fields = ("owner_id", "segment_id", "danger_category_id", "score")


@admin.register(DangerCategory)
class DangerCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "min_score", "max_score", "is_negative", "id")
    search_fields = ("name", "min_score", "max_score", "is_negative")
