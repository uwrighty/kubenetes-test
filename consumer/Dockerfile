FROM python:3 AS consumer

ADD src/consumer.py /

RUN pip install pika
RUN pip install Elasticsearch

CMD [ "python", "./consumer.py" ]
