#!/usr/bin/env python
import pika
from elasticsearch import Elasticsearch
import uuid


class Consumer:
    def __init__(self):
        self.es = Elasticsearch([{'host': 'db', 'port': 9200}])
        parameters = pika.URLParameters('amqp://user:password@queue:5672/%2F?connection_attempts=100&retry_delay=5')
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='raw_out')
        self.channel.queue_bind(exchange='raw', queue="raw_out")
        self.channel.basic_consume(self.callback, queue='raw_out', no_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        # post to database
        print(" [Raw Consumer] Received %r" % body)
        # post to db
        self.es.create(id=uuid.uuid4().hex, doc_type='text', index='books', body=body)


MyProcessor = Consumer()




