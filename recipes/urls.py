from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<id>/', views.recipe, name="recipe"),
]