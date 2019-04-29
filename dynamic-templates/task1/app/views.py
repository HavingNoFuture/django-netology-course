import os
import csv
import sys  

from django.shortcuts import render
from django.views.generic import TemplateView

from  django.conf import settings

class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста

        data = None
        with open('inflation_russia.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            data = list(reader)

        return render(request, self.template_name, {'data': data})
