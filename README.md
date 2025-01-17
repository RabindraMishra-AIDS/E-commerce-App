## Setup of Project
To initialize write: `django-admin startproject` `<Projectname>`.

To create a Application: `python manage.py startapp` `<Appname>`.

To run our Project on server: `python manage.py runserver`.

Update `Settings.py` file ie. include all applications in `INSTALLED_APPS`.

Add `templates` file to `DIRS` List present in `settings.py`.

Note: `/ == ''`  ie.(empty space)

## Learning Notes
- Refer to Bootstrap website to check colors supported by Bootstrap.
- We can use `{% extends "base.html" %}` this will help us to extend the base layout.
- We can use `{%load static%}` at the top of templates to load static files such as images,css,JS etc.
- We can use `{% block title%} {% endblock title %}` as template inheritance that a child template can override.