from fastapi import FastAPI
from .models import Item

app = FastAPI()


def __init__(self):
    pass


# v1=================================================================================================
# http://127.0.0.1:8000/
@app.get('/')
def index():
    return {'hello': 'word'}


# http://127.0.0.1:8000/v1/index
@app.get('/v1/index')
def index():
    return {'name': 'flack'}


# http://127.0.0.1:8000/v1/items/123?q=safdf
@app.get('/v1/items/{item_id}')
def get_items(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}


@app.put('/v1/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item_name': item.name}


@app.get('/v1/user/{uid}')
async def user(uid: str):
    return {
        'uid': uid,
        'name': 'flack',
        'age': 23,
        'address': 'shenzhen',
        'score': 100,
        'work': 10
    }


# async def app(scope, receive, send):
#     assert scope['type'] == 'http'
#
#     await send({
#         'type': 'http.response.start',
#         'status': 200,
#         'headers': [
#             [b'content-type', b'text/plain'],
#         ],
#     })
#     await send({
#         'type': 'http.response.body',
#         'body': b'Hello, world!',
#     })

# async def hello_world(message, channels):
#     content = b'<h1>Hello World</h1>'
#     resp = {
#         'status': 200,
#         'headers': [[b'content-type', b'text/html'], ],
#         'content': content,
#     }
#
#     await channels['reply'].send(resp)

def run():
    print('factory api running...')
    return app

# v1=================================================================================================
