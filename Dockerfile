FROM python:3.9.6-alpine3.14
LABEL maintainer="alekceyanatolievich@gmail.com"
WORKDIR /app
COPY . /app
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

ENV MYAPP_CITY=sankt-peterburg
ENV MYAPP_NAME=Guest
ENV FLASK_APP=myapphw2

CMD ["flask", "run", "--host", "0.0.0.0"]
