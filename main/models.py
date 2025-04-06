import os.path

from django.db import models
from django.urls import reverse


def room_img_path(instance, filename):
    return os.path.join('room_images', str(instance.room.id), filename)


def service_img_path(instance, filename):
    return os.path.join('service_images', str(instance.service.id), filename)


class RoomCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Room(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Номер комнаты")
    name = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    category = models.ForeignKey(RoomCategory, on_delete=models.DO_NOTHING, related_name="rooms",
                                 verbose_name="Категория")
    preview = models.ImageField("Превью", upload_to="room_previews/")

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"

    def get_absolute_url(self):
        return reverse('main:rooms_detail', kwargs={
            'room_type': self.category.name,
            'number': self.id,
        })


class Service(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="id услуги")
    name = models.CharField(max_length=100, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Изображение", upload_to=service_img_path)

    class Meta:
        verbose_name = "Фото-хранилище услуги"
        verbose_name_plural = "Фото-хранилище услуги"


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Изображение", upload_to=room_img_path)

    class Meta:
        verbose_name = "Фото-хранилище номера"
        verbose_name_plural = "Фото-хранилище номера"