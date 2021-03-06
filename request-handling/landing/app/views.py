from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()

def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing

    from_landing = request.GET.get('from-landing')
    counter_click[from_landing] += 1

    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов

    arg = request.GET.get('ab-test-arg')
    counter_show[arg] += 1
    if arg == 'test':
        return render_to_response('landing_alternate.html')

    return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    context = {}
    context['errors'] = {}
    
    if counter_show['original']:
        context['original_conversion'] = counter_click['original'] / counter_show['original']
    else:
        context['errors']['original'] = 'Оригинальная страница ни разу не просмотрена'

    if counter_show['test']:
        context['test_conversion'] = counter_click['test'] / counter_show['test']
    else:
        context['errors']['test'] = 'Тестовая страница ни разу не просмотрена'

    return render_to_response('stats.html', context)
