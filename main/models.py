import os.path

from django.db import models
from django.urls import reverse


def room_img_path(instance, filename):
    return os.path.join('room_images', str(instance.room.id), filename)


def service_img_path(instance, filename):
    return os.path.join('service_images', str(instance.service.id), filename)


def room_convenience_img_path(instance, filename):
    return os.path.join('room_convenience_icons', filename)


class ServicesManager(models.Manager):
    def special(self):
        return self.filter(isSpecial=True)

    def not_special(self):
        return self.filter(isSpecial=False)


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

    objects = models.Manager()

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"

    def __str__(self):
        return self.name

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
    isSpecial = models.BooleanField(verbose_name="Специальная услуга?", default=False)
    preview = models.ImageField("Превью", upload_to="services_previews/", blank=False)
    objects = models.Manager()
    manager = ServicesManager()

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


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


class RoomConvenience(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название удобства")
    image = models.ImageField("Иконка удобства", upload_to=room_convenience_img_path)
    rooms = models.ManyToManyField(Room, related_name="convenience")
    price = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "Удобства"
        verbose_name_plural = verbose_name
