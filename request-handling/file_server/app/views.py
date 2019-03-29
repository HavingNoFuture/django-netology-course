# import datetime
import time
import os

from django.shortcuts import render
from django.views.generic import TemplateView

from django.conf import settings


from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
print(datetime_object)

def create_datetime(tuple):
    return datetime(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4], tuple[5])

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
                'ctime': create_datetime(time.gmtime(info.st_ctime)),
                'mtime': create_datetime(time.gmtime(info.st_mtime))
            }

            if date:
                if sort_date == file_info['ctime'].date() or sort_date == file_info['mtime'].date():
                    result.append(file_info)
            else:
                result.append(file_info)
                
        return {
            'files': result,
            'date': sort_date
        }

def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:\
    filenames = os.listdir(settings.FILES_PATH)
    print()
    print(filenames)
    print(name in filenames)
    if name in filenames:
        with open(f'{settings.FILES_PATH}{os.sep}{name}') as file:
            file_content = file.read()
    else:
        file_content = 'Такого файла не сушествует!'

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )
