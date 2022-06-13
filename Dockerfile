# mostly copied from https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/
# pull official base image
FROM python:3.10.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

EXPOSE 5000

RUN ["chmod", "+x", "/usr/src/app/classified_ads_crud/docker-entrypoint.sh"]
ENTRYPOINT ["classified_ads_crud/docker-entrypoint.sh"]

