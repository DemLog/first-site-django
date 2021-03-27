from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': "Новостная страница"})


def vk(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'news/vk.html', {'news': news})