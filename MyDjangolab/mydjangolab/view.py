from django.http import HttpResponse
from django.shortcuts import render

import time


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
    # return HttpResponse('Hello World!')


def index(request):
    context = {}
    context['title'] = '数据列表vDb-VerticalContainer'
    context['flag'] = '10'
    context['isRead'] = False
    list = [10, 20, 30, 'flock']
    list2 = [100, 200, 300, 'feek']
    context['list'] = list
    context['list2'] = list2
    context['addtime'] = time.ctime(time.time())
    return render(request, 'index.html', context)



