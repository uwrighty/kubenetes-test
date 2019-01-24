#!/usr/bin/env python
import pika
from time import sleep

parameters = pika.URLParameters('amqp://user:password@queue:5672/%2F?connection_attempts=100&retry_delay=5')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='main')

with open("test.txt", "r") as f:
    for line in f:
        data = {'body': line}
        channel.basic_publish(exchange='',
                      routing_key='main',
                      body=data)
        print(" [x] Sent 'Message'")
        sleep(1)

connection.close()
