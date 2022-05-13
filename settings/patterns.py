'''
this file contains all texts' patterns that
users see on the interface.
'''


SENDING_MESSAGE = '\n\r[>>] SENDING MESSAGE: {}'

RECEIVED_MESSAGE = '\n\r[<<] RECEIVED MESSAGE: {}'

ERROR_MESSAGE = '\n\r[##] ERROR: {}'

INPUT = '\n\r[??] {}'

START_PRODUCING = '''
 _________________________________
|  STATUS : Start producing
|
|  Looking for a rabbit on :
|  HOST : %(host)s
|_ PORT : %(port)d'''

EXCHANGE_INFO = '''
 _________________________________
|  STATUS : Defined exhange
|
|  NAME : %(exchange_name)s:[%(exchange_type)s]
|_ ROUTING KEY : %(routing_key)s'''

START_CONSUMING = '''
 _________________________________
|  STATUS : Start consuming
|
|  Looking for a rabbit on :
|  HOST : %(host)s
|_ PORT : %(port)d'''

QUEUE_BIND = '''
 _________________________________
|  STATUS : Consuming a queue
|
|  NAME : %(exchange_name)s
|_ ROUTING KEY : %(routing_key)s'''