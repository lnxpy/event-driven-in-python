# notify.py
import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue = channel.queue_declare('order_notify')
queue_name = queue.method.queue

channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.notify'  # binding key
)

a = 0

def callback(ch, method, properties, body):
    global a
    print()
    print()
    print(body)
    print()
    print()

    payload = json.loads(body)
    a += 1
    print(' [x] Notifying {}'.format(payload))
    print(f' [x] Done no. {a}')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue_name, callback)

print(' [*] Waiting for notify messages. To exit press CTRL+C')

channel.start_consuming()