from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField(max_length=64, verbose_name='Модель телефона')
    price = models.IntegerField(verbose_name='Цена')
    image = models.TextField(verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField(max_length=64, verbose_name='Поддержка LTE')
    slug = models.SlugField(unique=True, verbose_name='URL Slug')
