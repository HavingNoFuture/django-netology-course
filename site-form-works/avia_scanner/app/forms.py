from django import forms
from django.urls import reverse_lazy

from .widgets import AjaxInputWidget
from .models import City
from django.forms.widgets import SelectDateWidget


class SearchTicket(forms.Form):
    first_city = forms.CharField(label="Город отправления:", widget=AjaxInputWidget(url=reverse_lazy('lookup'), attrs={'class': 'inline right-margin'}))
    last_city = forms.ModelChoiceField(label="Город прибытия:", queryset=City.objects.all(), empty_label = "-----")
    date = forms.DateField(label="Дата:", widget=SelectDateWidget)
