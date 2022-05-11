'''
this file containes all sort of settings you need
to config your application. Here you keep all your
settings and configurations.
'''

# exchange config
EXCHANGE = {
    'exchange_name': 'order',
    'exchange_type': 'direct',
    'routing_key': 'order.notify',
}

# message pattern
MESSAGE = {
    'amount': 5,
    'delay': 3,
    'context': [
        'id',
        'first_name',
        'last_name',
        'email',
    ],
}

RABBITMQ = {
    'host': 'localhost',
    'port': 5672
}