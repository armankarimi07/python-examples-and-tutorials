from fastapi import FastAPI
from fastapi.background import BackgroundTasks
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)


# this should be another database
redis = get_redis_connection(
    host="redis-10925.c338.eu-west-2-1.ec2.cloud.redislabs.com", # public endpoint of redis cloud database minus the port
    port=10925,
    password="RsdIhN1I7PjNH081n4WY7XNNQWL3kxdT", # password for 'default' user found in db configuration
    decode_responses=True # by default, all responses are returned as bytes in python, set to true to return as string
)


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    status: str # pending, completed, refunded
    
    class Meta:
        database = redis
        
        
@app.get('/orders/{pk}')
def get(pk: str):
    return Order.get(pk)
        
        
@app.post('/orders')
async def create(request: Request, background_tasks: BackgroundTasks):
    body = await request.json() # one way of getting the data from the body
    req = requests.get('http://localhost:8000/products/%s' % body['id'])
    product = req.json()
    order = Order(
        product_id=body['id'],
        price=product['price'],
        fee=0.2 * product['price'],
        total=1.2 * product['price'],
        quantity=body['quantity'],
        status='pending'
    )
    order.save()
    
    background_tasks.add_task(order_completed, order) # will be handled in background
    
    return order


import time
# Payment processing services
def order_completed(order: Order):
    time.sleep(5)
    order.status = 'completed'
    order.save()
    redis.xadd('order_completed', order.model_dump(), '*') # invoking redis stream event
    # the first arg is the key (name) of the event, second is just a value
    # third is a id, we set to * to get an auto generated id
    