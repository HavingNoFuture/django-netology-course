from django.shortcuts import render
from phones.models import Phone

def show_catalog(request):
    parameter = request.GET.get('sort')
    if parameter == 'name':
        phones = Phone.objects.order_by('name')
    elif parameter == 'min_price':
        phones = Phone.objects.order_by('price')
    elif parameter == 'max_price':
        phones = Phone.objects.order_by('-price')
    else: 
        phones = Phone.objects.all()

    print(da)
    context = {
        'phones': phones,
    }

    return render(
        request,
        'catalog.html',
        context
    )


def show_product(request, slug):
    phone = Phone.objects.get(slug = slug)

    context = {
        'phone': phone
    }
    return render(
        request,
        'product.html',
        context
    )

