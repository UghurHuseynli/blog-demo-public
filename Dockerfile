FROM python:3.10.0

RUN apt-get upgrade & apt update

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
