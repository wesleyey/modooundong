from django.contrib import admin
from .models import Place, Detail

# Register your models here.


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "address",
        "total_details",
        "rating",
        "creator",
    )
    list_filter = (
        "address",
        "details",
    )
    search_fields = (
        "name",
        "address",
        "details",
    )


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
