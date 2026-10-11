from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe, Category
from django.shortcuts import get_object_or_404
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
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'is_detail_page': False,
    })

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(category=category, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': category.name
    })

def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)

    if recipe.preparation_steps_is_html:
        recipe.preparation_steps = sanitizar_html(recipe.preparation_steps)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })