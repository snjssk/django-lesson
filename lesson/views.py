from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.http import require_GET, require_POST
from django.db.models import Q, Count
from rest_framework import viewsets, filters

from .models import Book
from .form import BookForm, BookModelForm
from .serializers import BookSerializer

import csv
import urllib.parse
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
    response = HttpResponse('<message>Hello</message>', content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename="hoge.xml"'
    return response


# csv
def res_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    writer.writerow([
        ['yamada', '山田', '30'],
        ['suzuki', '鈴木', '31'],
        ['satou', '佐藤', '32'],
    ])
    return response


# jsonの中身を返却
def res_json(request):
    return JsonResponse({
        'title': 'title',
        'price': '123'
    })


# クッキー保存
def setcookie(request):
    response = HttpResponse(render(request, 'lesson/setcookie.html'))
    response.set_cookie('app_title',
        urllib.parse.quote('titles'), 60 * 60 * 24 * 30)
    return response


# クッキー取得
def getcookie(request):
    app_title = urllib.parse.unquote(request.COOKIES['app_title']) if 'app_title' in request.COOKIES else '-'
    return render(request, 'lesson/getcookie.html', {
        'app_title': app_title
    })


# sesson
def setsesson(request):
    request.session['app_title'] = 'app_title_session'
    return HttpResponse('セッションを保存')


def getsesson(request):
    title = request.session['app_title'] \
        if 'app_title' in request.session else '-'
    return HttpResponse(title)


class MyTempView(TemplateView):
    # テンプレート名
    template_name = 'lesson/temp.html'
    # ビュー変数
    def get_context_data(self, **kwargs):
        # contextを取得
        context = super().get_context_data(**kwargs)
        # 取得したcontextにビュー変数を追加
        context['msg'] = 'Hello World!'
        return context

# form
def form_input(request):
    form = BookForm
    return render(request, 'lesson/form_input.html', {
        'form': form
    })


@require_POST
def form_process(request):
    form = BookForm(request.POST)
    # バリデーションチェック
    if form.is_valid():
        return render(request, 'lesson/form_process.html', {
            'form': form
        })
    else:
        return render(request, 'lesson/form_input.html', {
            'form': form
        })


# model
def crud_new(request):
    form = BookModelForm()
    return render(request, 'lesson/crud_new.html', {
        'form': form
    })


# @require_POST
# def crud_create(request):
#     obj = Book()
#     form = BookModelForm(request.POST, instance=obj)
#     if form.is_valid():
#         form.save()


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all() # 全てのデータを取得
    serializer_class = BookSerializer
