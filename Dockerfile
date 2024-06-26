FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./app /app/app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt
