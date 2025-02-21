from celery import Celery
import hashlib


app = Celery(
    name='tasks',
    broker_connection_retry_on_startup=True,
    broker="amqp://guest:guest@localhost:5672/",
    backend='rpc://'
)

@app.task
def BruteForce(password_hash, number):
    if hashlib.md5(str(number).encode()).hexdigest() == password_hash:
        return number
    return None
    
    
    