FROM python:3 AS producer

ADD src/producer.py /
ADD src/test.txt /

RUN pip install pika

CMD [ "python", "./producer.py" ]
