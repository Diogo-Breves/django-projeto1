from django.shortcuts import render, redirect
from . import forms
from django.http.response import Http404




def register_view(request):
    #if request.POST:
    register_form_data = request.session.pop('register_form_data', None)
    form = forms.RegisterForm(register_form_data)
    context= {'form': form}

    return render(request, 'authors/pages/register_view.html', context)


def register_create(request):
    if not request.method == 'POST':
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = {
        'first_name': POST.get('first_name', ''),
        'last_name': POST.get('last_name', ''),
        'username': POST.get('username', ''),
        'email': POST.get('email', ''),
    }
    
    form = forms.RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        del(request.session["register_form_data"])
        return redirect('authors:register')
    
    return render(
        request,
        'authors/pages/register_view.html',
        {'form': form}
    )