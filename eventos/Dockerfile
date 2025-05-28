FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /eventos/


COPY requirements.txt /eventos/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /eventos/

RUN python manage.py migrate --noinput


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
