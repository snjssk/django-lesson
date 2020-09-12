from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, Count

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


def filter(request):
    # filterにで条件を追加
    books = Book.objects.filter(price__gt=100)
    return render(request, 'lesson/list.html', {
        'books': books
    })

def get(request):
    # getは単一オブジェクト
    # 基本的には pk を指定してとる
    book = Book.objects.get(pk=1)
    return render(request, 'lesson/get.html', {
        'book': book
    })


def groupby(request):
    group = Book.objects.values('publisher')\
        .annotate(count=Count('publisher')).order_by('-count')

    return render(request, 'lesson/groupby.html', {
        'group': group,
        'count': group.count(),
        'exists': group.exists(),
    })
