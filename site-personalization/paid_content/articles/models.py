from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    paid_user = models.BooleanField()
    personality = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    paid = models.BooleanField()
