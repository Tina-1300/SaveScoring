# tasks.py
import time
from celery import Celery


app = Celery(
    name='tasks',
    broker_connection_retry_on_startup=True,
    broker="amqp://guest:guest@localhost:5672/",
    backend='rpc://'
)
#app.conf.broker_url = 'redis://localhost:6379/0'
#app.conf.broker_url = "amqp://guest:guest@localhost:5672/vhost"


@app.task
def multiply(x, y):
    time.sleep(1)
    return x* y
