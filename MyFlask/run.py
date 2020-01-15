#!flask/bin/python
# -*- coding:utf-8 -*-
from app import app
app.debug = True
#app.run(host='0.0.0.0') #这样用来监听所有的ip，团队调试用
app.run(host='127.0.0.1')
