from os import sys
import json

from pika import BlockingConnection, ConnectionParameters
from pika.exceptions import ConnectionClosedByBroker, AMQPConnectionError

from settings.configs import EXCHANGE, RABBITMQ
from settings.patterns import RECEIVED_MESSAGE, START_CONSUMING, QUEUE_BIND, INPUT



def callback(ch, method, properties, body):

    payload = json.loads(body)
    print(RECEIVED_MESSAGE.format(payload))
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    queue = channel.queue_declare('order_notify')
    queue_name = queue.method.queue

    print(START_CONSUMING % RABBITMQ)
    print(QUEUE_BIND % EXCHANGE)

    # TODO: reading from configs

    channel.queue_bind(
        exchange='order',
        queue=queue_name,
        routing_key='order.notify'  # binding key
    )
    
    channel.basic_consume(queue_name, callback)

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