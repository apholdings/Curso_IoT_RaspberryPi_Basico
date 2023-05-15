FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev cargo pkg-config

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

CMD python manage.py runserver 0.0.0.0:8000