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
    'amount': 20,
    'delay': 1,
    'context': [
        'id',
        'first_name',
        'last_name',
        'email',
    ],
}

# rabbitmq node
RABBITMQ = {
    'host': 'localhost',
    'port': 5672
}