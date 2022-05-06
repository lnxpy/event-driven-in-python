from pika import BlockingConnection, ConnectionParameters
from pika.exceptions import ConnectionWrongStateError, ConnectionClosedByBroker, AMQPConnectionError
import json
from faker import Faker
from os import sys
from constants import settings

def define_exchange(name, extype):
    try:
        return channel.exchange_declare(
            exchange=name,
            exchange_type=extype
        )
    except ConnectionClosedByBroker:
        sys.exit('make sure you have a proper configuration')

def main():
    exchange = define_exchange('order', 'direct') 
    print(exchange)

    fake = Faker()

    for _ in range(10):

        order = {
            'id': fake.ean(length=13),
            'name': fake.name()
        }
        
        channel.basic_publish(
            exchange='order',
            routing_key='order.notify',
            body=json.dumps({'order': order})
        )

        print(' [x] Sent notify message')

if __name__ == '__main__':

    try:
        connection = BlockingConnection(
            ConnectionParameters(
                'localhost',
                5672,
            )
        )
    except AMQPConnectionError:
        sys.exit('make sure your rabbitmq is running.')

    channel = connection.channel()
    main()
    connection.close()