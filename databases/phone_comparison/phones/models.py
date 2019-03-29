from django.db import models

# Create your models here.
class Producer(models.Model):
	name = models.TextField()
	country = models.TextField()

class Phone(models.Model):
	name = models.CharField(max_length=64, verbose_name='Модель телефона')
	price = models.IntegerField()
	os = models.CharField(max_length=64, verbose_name='Операционная система')
	resolution = models.CharField(max_length=64, verbose_name='Разрешение экрана')
	camera = models.CharField(max_length=64, verbose_name='Камера')
	ram = models.IntegerField()
	producer = models.ForeignKey('Producer',
on_delete=models.CASCADE)
