[![Build Status](https://travis-ci.org/jonstacks13/fibonacci.svg?branch=master)](https://travis-ci.org/jonstacks13/fibonacci)

# fibonacci

A Django Project with RESTful API to get the fibonacci numbers.

**Note**: Only tested on Python 3


## API

This project provides a RESTful API for getting back the first n fibonacci
numbers. It is located at ``/fibonacci/`` from the root url and returns a JSON
serialized response:

    GET /fibonacci/

By default, it will return to you a list of the first 10 fibonacci numbers. It
also accepts a query parameter q that allows you to specify how many fibonacci
numbers you would like. For instance:

    GET /fibonacci/?q=30

will return to you the first 30 fibonacci numbers

## Install

Install requirements with:

    pip install -r requirements/base.txt

Run Migrations:

    ./manage.py migrate

## Deployment

When deploying to production, I would suggest using something like gunicorn
and not the Django development server:

    pip install -r requirements/production.txt
    gunicorn fibonacci.wsgi -b 0.0.0.0:80

This will allow gunicorn to accept all incoming requests on port 80

### With Docker!

For easy deployment, a Dockerfile has been included which will allow you to
deploy to a number of PaaS or even locally if you are running docker. First,
you must build the image from the docker file:

    docker build -t fibonacci .

This will build you a new image thats ready for deployment! For convenience,
it is tagged as ``fibonacci``. To get the web service up and running, simply
run:

    docker run -d fibonacci

If you wish to bind to a different port other than the default of 80, you can
specify it with docker's ``-p`` flag. For instance, this command will run the
services locally on port 5000:

    docker run -d -p 5000:80 fibonacci

## Development

Install the development requirements with:

    pip install -r requirements/development.txt

Run Migrations:

    ./manage.py migrate

Start the development web server:

    ./manage.py runserver

This will start the Django development server running at ``localhost:8000``.
