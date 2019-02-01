FROM python:3 AS raw_consumer

ADD src/consumer.py /

RUN pip install pika
RUN pip install Elasticsearch

CMD [ "python", "./consumer.py" ]
