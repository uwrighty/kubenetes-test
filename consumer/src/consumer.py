#!/usr/bin/env python
import pika
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'db', 'port': 9200}])


def callback(ch, method, properties, body):
    # post to database
    es.create(index='all', body=body)
    print(" [x] Received %r" % body)


parameters = pika.URLParameters('amqp://user:password@queue:5672/%2F?connection_attempts=100&retry_delay=5')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='main')
channel.basic_consume(callback, queue='main', no_ack=True)






