# -*- coding: utf-8 -*-


from fastapi import FastAPI, Query, Path, Body, Cookie, Header, Form, File, UploadFile
from pydantic import BaseModel, Schema, UrlStr
from enum import Enum
from typing import List, Set, Dict

app = FastAPI()

# 需要一个ASGI服务器，用于生产如Uvicorn或Hypercorn


class ModelName(str, Enum):
    user = 'user'
    project = 'project'
    service = 'service'
    interface = 'interface'


class Image(BaseModel):
    url: UrlStr = None
    name: str = None


class Item(BaseModel):
    # item_id: int = Schema(..., ge=1, description='项目id')
    name: str
    price: float = Schema(..., gt=0, description='价格')
    description: str = Schema(None, title='描述', max_length=300)
    tax: float = None
    is_offer: bool = None
    # tags: list = []
    # tags: List[str] = []
    tags: Set[str] = set()
    # image: Image = None
    images: List[Image] = None


'''
@app.get()
@app.post()
@app.put()
@app.delete()
@app.options()
@app.head()
@app.patch()
@app.trace()
'''


@app.get('/')
def index():
    return {'fastapi': 'hello world'}


@app.get('/items/{item_id}')
def get_item(item_id: int = Path(..., title = '222', description = '项目id', ge = 1),
             q: str = Query(None, min_length = 2, max_length = 10, description = '参数'),
             p: List[str] = Query(['苹果', '香蕉', '桃子', '西瓜'])):
    return {'item_id': item_id, 'q': q, 'p': p}


"""
Query(None,
     min_length = 2,
     max_length = 10,
     regex = '^in',
     title = '123',
     description = 'test',
     alias = '456',
     deprecated=True
     )
"""


@app.put('/items/{item_id}')
async def update_item(*, item_id: int,
                      item: Item = Body(..., embed = True, example = {
                          'name': 'Foo',
                          'price': 20.00,
                          'description': '描述',
                          'tax': 2.22,
                          'is_offer': True
                      },)):
    # return {'item_name': item.name, 'item_id': item_id}

    res = item.dict()
    res.update({'item_id': item_id})

    # res = item
    # res.item_id = item_id
    # print(res.item_id)

    return res


@app.get('/user/{id}')
async def get_user(uid: str = None):
    return {'id': uid, 'username': 'flack', 'nickname': 'michaeltuling', 'phone': '15599999999'}


@app.get('/model/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.user:
        return {'model_name': model_name, 'message': '用户'}
    if model_name.value == 'project':
        return {'model_name': model_name, 'message': '项目'}
    if model_name == ModelName.interface:
        return {'model_name': model_name, 'message': '接口'}

    return {'model_name': model_name, 'message': '服务'}


@app.get('/files/{file_path:path}')
def read_user_me(file_path: str):
    return {'file_path': file_path}


@app.post('/files/')
async def create_file(file: bytes = File(...)):
    return {'file_size': len(file)}


@app.post('/uploadfile/')
async def create_upload_file(file: UploadFile = File(...)):
    # with open(file.filename, 'wb') as f:
    #     f.write(file)

    return {'file': file}

