from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Olá, mundo!")

def home(request):
    context = {
        'name' : 'Diogo Breves',
        }
    return render(request, 'recipes/pages/home.html', context)

