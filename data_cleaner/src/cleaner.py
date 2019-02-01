#!/usr/bin/env python
import pika
import json


class Cleaner:
    def __init__(self):
        parameters = pika.URLParameters('amqp://user:password@queue:5672/%2F?connection_attempts=100&retry_delay=5')
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='raw_clean')
        self.channel.queue_bind(exchange='raw', queue="raw_clean")
        self.channel.basic_consume(self.callback, queue='raw_clean', no_ack=True)
        self.channel.exchange_declare(exchange='clean', exchange_type='fanout')
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        # post to database
        print(" [Cleaner] Received %r" % body)

        data = json.loads(body)

        temp = data['body'].split()
        temp = ' '.join(temp)

        data['body'] = temp
        print(" [Cleaner] Processed %r" % body)

        # if the length of message is 0 then dont write any other message else.
        if len(temp.strip()) == 0:
            print(" [Cleaner] Nothing to write  %r" % body)
        else:
            self.channel.basic_publish(exchange='clean',
                      routing_key='', body=json.dumps(data))

MyProcessor = Cleaner()




