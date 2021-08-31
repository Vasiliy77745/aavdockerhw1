#!/bin/bash

mkdir ~/dockertest1 && cd ~/dockertest1

git init .

git pull git@github.com:Vasiliy77745/aavdockerhw1.git

export TAG=$(git rev-parse --abbrev-ref HEAD)-$(git rev-parse --short HEAD)

docker build -t alexv77745/hw2:$TAG .

docker-compose up -d

docker push alexv77745/hw2:$TAG

