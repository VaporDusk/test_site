from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения first_app.")

def second_function(request):
    return HttpResponse("<h1>Заголовок страницы</h1>")
