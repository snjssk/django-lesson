from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
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


def review(request):
    return render(request, 'lesson/review.html', {
        'book': Book.objects.get(pk=1)
    })


# idを受け取る
def root_param(request, id):
    # クエリ情報
    keyword = request.GET['keyword']
    return HttpResponse(f' id: {id}, keyword: {keyword}')


# リクエストヘッダー
def req_header(request):
    ua = request.headers['User-Agent']
    return HttpResponse(f' ua:{ua}')


# リダイレクト
def req_redirect(request):
    return redirect('list')


# 404
# get_object_or_404 で簡略化できる
def res_notfound(request):
   try:
        books = Book.objects.get(pk=100)
    except Book.DoesNotExist:
        raise Http404('ありません')
    return render(request, 'lesson/list.html', {
        'book': books
    })


# レスポンスヘッダー
def res_header(request):
    response = HttpResponse('')