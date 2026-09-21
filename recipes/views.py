from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'name' : 'Diogo Breves',
        }
    return render(request, 'recipes/pages/home.html', context)

def recipe(request, id):
    context = {
            'name' : 'Diogo Breves',
            }
    return render(request, 'recipes/pages/recipe-view.html', context)