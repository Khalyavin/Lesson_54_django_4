from django.shortcuts import render

from catalog.models import Product


def catalog(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/index.html', context)

def contacts(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('price'))

    return render(request, 'catalog/contacts.html')