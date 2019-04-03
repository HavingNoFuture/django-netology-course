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

        database = []
        headers = []
        with open(f'{settings.BASE_DIR}{os.sep}inflation_russia.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')

            flag = True
            for row in reader:
                year = []
                keys = row.keys()
                 
                for key in keys:
                    month = {}
                    if row[key]:
                        if key == 'Год':
                            month['count'] = int(row[key])
                        else:
                            month['count'] = float(row[key])
                        month['key'] = key

                    else:
                        month['count'] = '-'
                        month['key'] = key
                                    
                    year.append(month)

                    if flag:
                        headers.append(key)

                flag = False
                database.append(year)

        context = {'data': database, 'headers': headers}
        return render(request, self.template_name,
                      context)
