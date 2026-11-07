from django.shortcuts import render, redirect
from . import forms
from django.http.response import Http404



def register_view(request):
    #if request.POST:
    register_form_data = request.session.pop('register_form_data', None)
    form = forms.RegisterForm(register_form_data)
    context= {'form': form}

    print(
    "Password presente?",
    'password' in (register_form_data or {})
    )
    print("Formulário válido?", form.is_valid())
    print("Erros:", form.errors)

    return render(request, 'authors/pages/register_view.html', context)


def register_create(request):
    if not request.method == 'POST':
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = forms.RegisterForm(POST)
    return redirect('authors:register')