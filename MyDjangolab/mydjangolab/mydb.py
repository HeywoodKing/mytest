# -*- coding: UTF-8 -*-

from django.http import HttpResponse

from MyModel.models import MyDjangoLab
import time

# 数据库操作
def savedb(request):
    my = MyDjangoLab(name='run', sex='女', age='36', email='ching125@126.com', addtime='2017041002')
    # my = MyDjangoLab(name='run', sex='女')
    my.save()
    return HttpResponse("<p>数据添加成功！</p>")

# 数据库操作
def getdb(request):
    # 初始化
    response = ''
    response1 = ''

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = MyDjangoLab.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = MyDjangoLab.objects.filter(id=1)

    # 获取单个对象
    response3 = MyDjangoLab.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    MyDjangoLab.objects.order_by('name')[0:2]

    # 数据排序
    MyDjangoLab.objects.order_by('id')

    # 上面的方法可以连锁使用
    MyDjangoLab.objects.filter(name='run').order_by('id')

    # 输出所有数据
    for var in list:
        response1 += var.name + ' '

    response = response1
    return HttpResponse("<p>" + response + "</p>")

# 数据库操作
def updatedb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    res = MyDjangoLab.objects.get(id=1)
    res.name = 'Google'
    res.save()

    # 另外一种方式
    # MyDjangoLab.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # MyDjangoLab.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")

# 数据库操作
def deletedb(request):
    # 删除id=1的数据
    res = MyDjangoLab.objects.get(id=1)
    res.delete()

    # 另外一种方式
    MyDjangoLab.objects.filter(id=1).delete()

    # 删除所有数据
    MyDjangoLab.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")


