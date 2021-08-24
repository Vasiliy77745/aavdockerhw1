FROM python:3.9.6-alpine3.14

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

ENV FLASK_APP=myapp

CMD ["flask", "run", "--host", "0.0.0.0"]
