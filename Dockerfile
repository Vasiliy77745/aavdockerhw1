FROM python:3.9.6-alpine3.14

RUN pip install flask requests

RUN mkdir /app

COPY myapp.py /app

WORKDIR /app

ENV FLASK_APP=myapp

CMD ["flask", "run", "--host", "0.0.0.0"]
