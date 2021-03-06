CherryMusic
===========
[![Build Status](https://travis-ci.org/pando85/cherrymusic.svg?branch=devel-django)](https://travis-ci.org/pando85/cherrymusic)

This is a rewrite of CherryMusic based on django.

You can test it at:
http://music.openrock.mooo.com/
* User: `test`
* Password: `1234`

Setup
-----

Configure `config.yml` with your music directories:
* One path:
```docker-compose
web:
  volumes:
    - /home/user/My Music:/usr/src/app/music:ro
```
* Multiple paths:
```docker-compose
web:
  volumes:
    - /home/user/Classic Music:/usr/src/app/music/Classic:ro
    - /home/user/Punk Music:/usr/src/app/music/Punk:ro
```

Install dependencies:
* docker
* docker-compose>=1.5.0

Create containers:
```bash
docker-compose build
docker-compose up -d
```

Initialice database:
```bash
docker-compose run --rm web python3 manage.py migrate auth
docker-compose run --rm web python3 manage.py migrate 
```

Default admin user: `admin/admin`

Reinstall cherrymusic
---------------------
```bash
docker-compose stop
docker-compose rm
```
And then reinstall.


Update cherrymusic
------------------
```bash
docker-compose stop
docker-compose rm web
docker-compose build
docker-compose up -d
```

Development frotent
-------------------
To install and run development containers:
```bash
docker-compose stop
docker-compose -f development.yml build
docker-compose -f development.yml up -d
```

Install bower components:
```bash
docker-compose -f development.yml run  --rm web_dev python3 manage.py bower_install -- --allow-root
```
Update static files
-------------------
In development mode:

In `./web`:
```bash
docker-compose -f development.yml run --rm web_dev python3 manage.py collectstatic
```

Tests
-----
To install test containers:
```bash
docker-compose stop
docker-compose -f test.yml build
```

Test server:
```bash
docker-compose -f test.yml run --rm web_test /usr/src/test.sh && \
docker-compose -f test.yml stop
```