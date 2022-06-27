from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. aqui se escribe el codigo python
from webapp.models import *

def bienvenido(request):
    #return HttpResponse('Hola mundo desde Django')
    persona = Persona.objects.all()
    return render(request, 'index.html', {'persona': persona})


def despedida(request):
    return HttpResponse('Despedida desde Django')



