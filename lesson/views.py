from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello world')


def temp(request):
    # ビュー変数、辞書型
    context = {
        'msg': 'hello world'
    }
    return render(request, 'lesson/temp.html', context)
