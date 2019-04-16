import os
from datetime import datetime

from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from django.conf import settings


class FileList(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:

        filenames = os.listdir(settings.FILES_PATH)

        if date:
            sort_date = datetime.strptime(date, '%Y-%m-%d').date()

        result = []
        for filename in filenames:
            info = os.stat(f'{settings.FILES_PATH}{os.sep}{filename}') # Получаю информацию о файле

            file_info = {
                'name': filename,
                'ctime': datetime.fromtimestamp(info.st_ctime),
                'mtime': datetime.fromtimestamp(info.st_mtime)
            }

            if date is None or sort_date == file_info['ctime'].date() or sort_date == file_info['mtime'].date():
                result.append(file_info)

        context = {'files': result}
        if date:
            context['date'] = sort_date 

        return context

def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:\
    filenames = os.listdir(settings.FILES_PATH)

    if name in filenames:
        with open(f'{settings.FILES_PATH}{os.sep}{name}') as file:
            file_content = file.read()
    else:
        raise Http404("File does not exist")

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )
