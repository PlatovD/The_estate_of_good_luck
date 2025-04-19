from django.contrib import admin

from .models import Room, RoomCategory, RoomImage, Service, ServiceImage, RoomConvenience


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_display_links = ('id', 'name')
    ordering = ['name']
    list_editable = ('price',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name')
    ordering = ['name']
    list_editable = ('price',)


@admin.register(RoomCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(RoomConvenience)
class RoomConvenienceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk', 'name',)


admin.site.register(RoomImage)
admin.site.register(ServiceImage)
