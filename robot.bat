Scripts\activate

cd .\test\nico

celery -A tasks:app worker --loglevel=INFO -P gevent

PAUSE
