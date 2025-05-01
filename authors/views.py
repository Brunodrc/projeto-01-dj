from django.shortcuts import render, redirect
from django.http import Http404
from .forms import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'authors/pages/register_view.html', {
        'form': form
    })

# é preciso criar uma view para receber o post do formulário
# essa view vai ler e validar os dados, ou seja, não renderiza nada
# separação das funções


def register_create(request):

    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(request.POST)

    return redirect('authors:register')
