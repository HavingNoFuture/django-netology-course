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
    if from_landing == 'original':
        counter_click['original_click'] += 1
    elif from_landing == 'test':
        counter_click['test_click'] += 1

    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов

    arg = request.GET.get('ab-test-arg')
    if arg == 'original':
        counter_show['original_show'] += 1
    elif arg == 'test':
        counter_show['test_show'] += 1
        return render_to_response('landing_alternate.html')

    return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    if counter_show['original_show']:
        original_conversion = counter_click['original_click'] / counter_show['original_show']
    else:
        original_conversion = 'Оригинальная страница ни разу не просмотрена'

    if counter_show['test_show']:
        test_conversion = counter_click['test_click'] / counter_show['test_show']
    else:
        test_conversion = 'Тестовая страница ни разу не просмотрена'



    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })

