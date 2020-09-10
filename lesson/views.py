from django.shortcuts import render
from django.http import HttpResponse

from .models import Book

import random


def index(request):
    return HttpResponse('hello world')


def temp(request):
    # ビュー変数、辞書型
    context = {
        'msg': 'hello world'
    }
    return render(request, 'lesson/temp.html', context)


def list(request):
    # all()は全件
    books = Book.objects.all()
    return render(request, 'lesson/list.html', {
        'books': books
    })


def iftag(request):
    return render(request, 'lesson/iftag.html', {
        'random': random.randint(0, 100),
        'flag': True,
        'weeks': ['月', '火', '水', '木', '金', '土', '日'],
        'empties': []
    })