from django.shortcuts import render
from django.http.response import Http404
from utils.recipes.factory import make_recipe
from .models import Recipe, Category
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from utils.pagination import make_pagination
from django.contrib import messages
import nh3

def sanitizar_html(conteudo):
    tags_permitidas = {
        "p",
        "br",
        "strong",
        "em",
        "h2",
        "h3",
        "ul",
        "ol",
        "li",
    }

    return nh3.clean(
        conteudo,
        tags=tags_permitidas,
        attributes={},
    )

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    #bloco de programação própria
    paginator = Paginator(recipes, 3)
    numero_pagina = request.GET.get('page')
    pagina = paginator.get_page(numero_pagina)
    
    numeros = paginator.get_elided_page_range(number=pagina.number, on_each_side=2, on_ends=1)


    return render(request, 'recipes/pages/home.html', context={
        'recipes': pagina,
        'is_detail_page': False,
        'numeros': numeros,
    })

def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(category=category, is_published=True).order_by('-id')

    #bloco de programação própria
    paginator = Paginator(recipes, 2)
    numero_pagina = request.GET.get('page')
    pagina = paginator.get_page(numero_pagina)

    numeros = paginator.get_elided_page_range(number=pagina.number, on_each_side=2, on_ends=1)
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': pagina,
        'title': category.name,
        'numeros': numeros,
    })

def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)

    if recipe.preparation_steps_is_html:
        recipe.preparation_steps = sanitizar_html(recipe.preparation_steps)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

def search(request):
    search_term = request.GET.get('q', '').strip()
    
    recipes = Recipe.objects.none()

    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(category__name__icontains=search_term) |
            Q(author__username__icontains=search_term) |
            Q(author__first_name__icontains=search_term) |
            Q(author__last_name__icontains=search_term),
            is_published=True
        ).order_by('-id')

    quantidade = recipes.count()

    #bloco de programação própria
    paginator = Paginator(recipes, 2)
    numero_pagina = request.GET.get('page')
    pagina = paginator.get_page(numero_pagina)

    numeros = paginator.get_elided_page_range(number=pagina.number, on_each_side=2, on_ends=1)
    
    context={
        'recipes': pagina,
        'search_term': search_term,
        'page_title': search_term,
        'quantidade': quantidade,
        'numeros': numeros,
        'search_pag': f'&q={search_term}'
    }
    return render(request, 'recipes/pages/search.html', context)