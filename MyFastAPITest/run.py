
from myfastapitest import factory

app = factory.run()


# 您还需要一个ASGI服务器，用于生产如Uvicorn或Hypercorn。
# uvicorn main:app --reload
"""
该命令uvicorn main:app指的是：
main：文件main.py（Python“模块”）。
app：main.py在线内创建的对象app = FastAPI()。
--reload：在代码更改后使服务器重新启动。只有这样才能发展。

uvicorn --host 127.0.0.1 --port 8080 run:app --reload
"""
