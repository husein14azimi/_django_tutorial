from django.shortcuts import render
from django.utils import timezone
from django.db.models import F
from .models import Person, OwnerFamily, Holding, Company

def homepage(request):
    return render(request=request, template_name='home.html')







def temp(request):


    queryset_2 = OwnerFamily.objects.filter(holding__name = 'holding1')
    queryset = Holding.objects.filter(company__name = '1company1')


    context = {
        'owner_families': queryset_2,
        'holdings': queryset,
    }
    return render(request=request, template_name='temp.html', context=context)






def persons(request):
    query = Person.objects.all()

    context = {
        'persons':query
    }
    return render(request=request, template_name='persons.html', context=context)

def person(request, id):
    item = Person.objects.get(id=id)

    context = {
        'person':item,
        'id':id,
    }
    return render(request=request, template_name='person.html', context=context)
    