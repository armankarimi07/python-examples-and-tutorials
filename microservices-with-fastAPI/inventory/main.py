from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)

redis = get_redis_connection(
    host="redis-10925.c338.eu-west-2-1.ec2.cloud.redislabs.com", # public endpoint of redis cloud database minus the port
    port=10925,
    password="RsdIhN1I7PjNH081n4WY7XNNQWL3kxdT", # password for 'default' user found in db configuration
    decode_responses=True # by default, all responses are returned as bytes in python, set to true to return as string
)


class Product(HashModel):
    name: str
    price: float
    quantity: int
    
    class Meta:
        database = redis
    

@app.get("/")
async def root():
    return {"message": "Hellw world"}

@app.get('/products')
def all():
    return [format(pk) for pk in Product.all_pks()]


def format(pk: str):
    product = Product.get(pk)
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.post('/products')
def create(product: Product):
    return product.save()


@app.get('/products/{pk}')
def get(pk: str):
    return Product.get(pk)


@app.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)