from django.shortcuts import render, redirect
from .forms import ArticlesForm, BooleanFieldFrom


def index(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена не верно'

    form = ArticlesForm()
    checkbox = BooleanFieldFrom()
    data = {
        'form': form,
        'error': error,
        'checkbox': checkbox
    }

    return render(request, 'index/index.html', data)


def contact(request):
    return render(request, 'contact/contact.html')
