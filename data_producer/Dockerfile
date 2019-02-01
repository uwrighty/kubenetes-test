FROM python:3 AS raw_producer

ADD src/producer.py /
ADD src/test.txt /

RUN pip install pika

CMD [ "python", "./producer.py" ]
