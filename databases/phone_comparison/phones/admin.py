from django.contrib import admin
from .models import Phone, Producer


# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'os')

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
	list_display = ('name',)