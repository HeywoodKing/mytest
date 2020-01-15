# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf


# 表单
def search_form(request):
    return render(request, 'get.html')


# 接收到的数据请求处理
# 接收请求数据
def search_get(request):
    request.encoding = 'utf-8'

    if 'q' in request.GET:
        message = '你搜索的内容为：' + request.GET['q'] + '<br>' \
                  + 'path:' + request.path + '<br>' \
                  + 'get_full_path():' + request.get_full_path() + '<br>' \
                  + 'is_secure():' + str(request.is_secure()) + '<br>' \
                  + 'method:' + request.method + '<br>' \
                  + 'GET:' + str(request.GET) + '<br>' \
                  + 'POST:' + str(request.POST) + '<br>' \
                  + 'COOKIES:' + str(request.COOKIES) + '<br>' \
                  + 'FILES:' + str(request.FILES) + '<br>' \
                  + 'META:' + str(request.META) + '<br>' \
                  + 'session:' + str(request.session) + '<br>' \
                  + 'user:' + str(request.user) + '<br>'
        if request.user.is_authenticated():
            message += '登陆了'
        else:
            message += '未登陆'

    else:
        message = '你提交了空表单'

    return HttpResponse(message)


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']

    return render(request, "post.html", ctx)


