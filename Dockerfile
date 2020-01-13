#FROM python:3
#ENV PYTHONUNBUFFERED 1
#RUN mkdir /code
#WORKDIR /code
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
#COPY . /code/
#

FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  && apk upgrade \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Brotli dependency
  && apk add g++

# Requirements are installed.
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/

## Least priviliged user
#RUN mkdir /app
#RUN addgroup -S django \
#    && adduser -S -G django django
#WORKDIR /app
#COPY . /app
#RUN chown -R django:django /app
#USER django
