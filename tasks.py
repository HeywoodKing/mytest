from datetime import datetime
from invoke import task


@task
def httpd(c, port=8888):
    print('*' * 50)
    print('author:hywell')
    print('date:{}'.format(datetime.now()))
    print('*' * 50)
    print('http服务已启动')
    c.run('python3 -m http.server {port}'.format(port=port))
