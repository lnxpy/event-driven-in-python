from pika import BlockingConnection, ConnectionParameters
from pika.exceptions import ConnectionWrongStateError, ConnectionClosedByBroker, AMQPConnectionError
import json
from os import sys
from settings.constants import volumes
from settings.configs import EXCHANGE, MESSAGE

from time import sleep


def define_exchange(exchange_name, exchange_type):
    try:
        return channel.exchange_declare(
            exchange=exchange_name,
            exchange_type=exchange_type
        )
    except ConnectionClosedByBroker:
        sys.exit('make sure you have a valid configuration')

def main():
    exchange = define_exchange(
        exchange_name=EXCHANGE['exchange_name'],
        exchange_type=EXCHANGE['exchange_type']
    )

    for _ in range(MESSAGE['amount']):
        body = {}
        for _ in MESSAGE['context']:
            body[_] = volumes[_]()

        channel.basic_publish(
            exchange=EXCHANGE['exchange_name'],
            routing_key=EXCHANGE['routing_key'],
            body=json.dumps(body)
        )

        print(' [x] Sent notify message')


if __name__ == '__main__':

    try:
        # TODO: reading from configs
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
