#!/usr/bin/env python
import pika
from time import sleep
import json


parameters = pika.URLParameters('amqp://user:password@queue:5672/%2F?connection_attempts=100&retry_delay=5')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange='raw',
                         exchange_type='fanout')
channel.queue_declare(queue='raw')


with open("test.txt", "r") as f:
    for line in f:
        # create json
        data = {}
        data['body'] = line

        channel.basic_publish(exchange='raw',
                      routing_key='',
                      body=json.dumps(data))
        print(" [Producer] Sent Message " + str(json.dumps(data)))
        sleep(1)

connection.close()
