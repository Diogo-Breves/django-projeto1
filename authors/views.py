from django.shortcuts import render, redirect
from . import forms
from django.http.response import Http404
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


def register_view(request):
    #if request.POST:
    register_form_data = request.session.get('register_form_data', None)
    form = forms.RegisterForm(register_form_data)
    context= {'form': form}
    return render(request, 'authors/pages/register_view.html', context)


def register_create(request):
    if not request.method == 'POST':
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = forms.RegisterForm(POST)
    return redirect('authors:register')