from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('sobre/', views.my_view),
    path('', views.home),
]