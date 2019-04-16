from django.contrib import admin
from django.db import models
from .models import Car, Review
from .forms import ReviewAdminForm
from ckeditor.widgets import CKEditorWidget

class CarAdmin(admin.ModelAdmin):
    # fields = ('brand')
    list_display = ('brand', 'model', 'review_count')
    list_filter = ('id', 'brand')
    search_fields = ('brand', 'model')
    sortable_by = 'id'

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'title', )
    list_filter = ('car',)
    search_fields = ('title', 'car__model')
    sortable_by = 'id'
    form = ReviewAdminForm




admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
