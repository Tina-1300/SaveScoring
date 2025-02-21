# producer.py
from tasks import multiply

for i in range(100):
    result = multiply.delay(2, 3)

    print(result.get())
