from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Главная страница приложения django',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'Здесь будет информация о репетиторе',
    }

    return render(request, 'about/index.html', context)

def contacts(request):
    context = {
        'title': 'Контакты',
        'content': 'Здесь будет информация о всех соцсетях, номерах и т.д. репетитора',
    }

    return render(request, 'contacts/index.html', context)

def singUp(request):
    context = {
        'title': 'Записаться',
        'content': 'Здесь будет форма для записи на урок к репетитору по матемитике',
    }

    return render(request, 'singUp/index.html', context)

def reviews(request):
    context = {
        'title': 'Отзывы',
        'content': 'Здесь будет список отзывов о репетиторе по математике',
        'get_params': request.GET
    }

    return render(request, 'reviews/index.html', context)