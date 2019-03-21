import datetime
import time
import os

from django.shortcuts import render
from django.views.generic import TemplateView

from app.settings import FILES_PATH


def create_datetime(tuple):
    return datetime.datetime(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4], tuple[5])

class FileList(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:

        filenames = os.listdir(FILES_PATH)

        if date:
            sort_date_tuple = time.strptime(date, '%Y-%m-%d') # Перевожу строку даты в struct_mode обьект
            sort_date = create_datetime(sort_date_tuple).date() # Преобразую этот обьект в дату без времени

        result = []
        for filename in filenames:
            info = os.stat(f'{FILES_PATH}{os.sep}{filename}') # Получаю информацию о файле

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
                
        if date:
            return {
                'files': result,
                'date': sort_date
            }
        else:
            return {
                'files': result
            }


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:\
    with open(f'{FILES_PATH}{os.sep}{name}') as file:
        file_content = file.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )
