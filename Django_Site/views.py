from django.shortcuts import render
from .models import Author, CrosswordBase
from django.views import generic
import datetime
import random

list_of_error = [
    'Вы кто такие? Я вас не звал. Идите нахуй!',
    'Кто это у нас такой люботный и полез, куда не просят?',
    'Лок тар о гар!',
    'Юра, хватит обновлять страницу с ошибкой!',
    'Не учатся ничему некоторые и учиться не хотят...',
    'Семь раз отмерь, один раз "такой страницы не существует"',
    'Факир был пьян, и фокус не удался',
    'Прости, Марио, но твои кроссворды в другом замке',
    'Тоже захотел посмотреть на Рикардо Милоса?',
    'Ну давай, введите неправильный url ещё раз'
]


def main_page(request):
    num_crosswords = CrosswordBase.objects.all().count()
    num_authors = Author.objects.all().count()
    return render(request, 'main.html', context={
        'num_crosswords': num_crosswords,
        'num_authors': num_authors
    })


def error_page(request):
    error_text = list_of_error[random.randint(0, len(list_of_error) - 1)]
    num_errors = request.session.get('num_errors', 0) + 1
    request.session['num_errors'] = num_errors
    return render(request, 'error.html', context={
        'error_text': error_text,
        'num_errors': num_errors
    })


class CrosswordDetailedView(generic.DetailView):
    model = CrosswordBase


class CrosswordView(generic.ListView):
    model = CrosswordBase
    paginate_by = 1

    def get_queryset(self, **kwargs):
        return CrosswordBase.objects.order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CrosswordView, self).get_context_data(**kwargs)
        context['Current_Date'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        return context
