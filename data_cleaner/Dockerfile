FROM python:3 AS cleaner

ADD src/cleaner.py /

RUN pip install pika

CMD [ "python", "./cleaner.py" ]
