from os import sys
import json

from pika import BlockingConnection, ConnectionParameters
from pika.exceptions import AMQPConnectionError

from settings.configs import EXCHANGE, RABBITMQ
from settings.patterns import RECEIVED_MESSAGE, START_CONSUMING, QUEUE_BIND, INPUT


def async_consume(ch, method, properties, body):
    payload = json.loads(body)
    print(RECEIVED_MESSAGE.format(json.dumps(payload, indent=2)))
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    queue = channel.queue_declare('order_notify')
    queue_name = queue.method.queue

    print(START_CONSUMING % RABBITMQ)
    print(QUEUE_BIND % EXCHANGE)

    channel.queue_bind(
        exchange=EXCHANGE['exchange_name'],
        queue=queue_name,
        routing_key=EXCHANGE['routing_key']
    )
    
    channel.basic_consume(queue_name, async_consume)
    print(INPUT.format('Listening to queue for messages.. (press CTRL+C to exit)'))
    channel.start_consuming()



if __name__ == '__main__':
    try:
        connection = BlockingConnection(
            ConnectionParameters(**RABBITMQ)
        )
    except AMQPConnectionError:
        sys.exit(ERROR_MESSAGE.format('Make sure the rabbitmq node is running.'))

    channel = connection.channel()
    main()
    connection.close()