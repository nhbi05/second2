from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

#
# Create your views here.
def homePage(request):
    list_sitters = Sitter.objects.all()
    list_babies = Baby.objects.all()
    count_babies = len(list_babies)
    contxt = {
        'list_sitters': list_sitters,
        'list_babies': list_babies,
        'total_babies': count_babies,
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(contxt))


def babiesList(request):
    template = loader.get_template('babies_list.html')
    return HttpResponse(template.render())

def sittersList(request):
    template = loader.get_template('list_sitters.html')
    return HttpResponse(template.render())

def payments(request):
    template = loader.get_template('payments.html')
    return HttpResponse(template.render())

def procurement(request):
    template = loader.get_template('procurement.html')
    return HttpResponse(template.render())