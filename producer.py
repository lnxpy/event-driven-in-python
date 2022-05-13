import json
from os import sys
from time import sleep

from pika import BlockingConnection, ConnectionParameters
from pika.exceptions import ConnectionClosedByBroker, AMQPConnectionError

from settings.constants import volumes
from settings.configs import EXCHANGE, MESSAGE, RABBITMQ
from settings.patterns import SENDING_MESSAGE, ERROR_MESSAGE, START_PRODUCING, EXCHANGE_INFO, INPUT


def define_exchange(exchange_name, exchange_type):
    try:
        return channel.exchange_declare(
            exchange=exchange_name,
            exchange_type=exchange_type
        )
    except ConnectionClosedByBroker:
        sys.exit(ERROR_MESSAGE.format('Make sure you have a valid configuration.'))

def main():
    exchange = define_exchange(
        exchange_name=EXCHANGE['exchange_name'],
        exchange_type=EXCHANGE['exchange_type']
    )

    print(START_PRODUCING % RABBITMQ)
    print(EXCHANGE_INFO % EXCHANGE)

    try:
        input(INPUT.format('Press to start producing..'))
    except KeyboardInterrupt:
        sys.exit()
        connection.close()

    for _ in range(MESSAGE['amount']):
        body = {}
        for _ in MESSAGE['context']:
            body[_] = volumes[_]()

        channel.basic_publish(
            exchange=EXCHANGE['exchange_name'],
            routing_key=EXCHANGE['routing_key'],
            body=json.dumps(body)
        )

        print(SENDING_MESSAGE.format(list(body.values())[0]))
        print(json.dumps(body, indent=2))
    
        # TODO: using Pydantic for serialization

        try:
            sleep(MESSAGE['delay'])
        except KeyError:
            pass


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
