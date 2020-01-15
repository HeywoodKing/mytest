# -*- coding: UTF-8 -*-

# CGi处理模块
import cgi
import cgitb


# 创建FieldStorage的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print('Content-Type:text/html')
print('')
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title>Hello World CGI - 我的第一个CGI程序</title>')
print('</head>')
print('<body>')
print('<h2>Hello World! 我是来自aforge的第一个CGI程序</h2>')
print('<h3>%s官网：%s</h3>' % (site_name, site_url))
print('</body>')
print('</html>')







