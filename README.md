# your-repo
your-repo

-> clone your repo in specific dir
(specific-dir)>>> git clone https://github.com/<user-name>/<your-repo>.git

-> go to the base dir
(specific-dir)>>> cd <base-dir>

-> create virtual environment
...<base-dir>>>> python -m venv [virtual-env-name]

-> activate and de-activate your virtual env.
...<base-dir>>>> [virtual-env-name]\Scripts\activate
([virtual-env-name])...<base-dir>>>> [virtual-env-name]\Scripts\deactivate

-> make sure you have installed python in your system
([virtual-env-name])...<base-dir>>>> python --version
Python 3.12.2

-> Now install django in your virtual env.
([virtual-env-name])...<base-dir>>>> pip install Django
([virtual-env-name])...<base-dir>>>> python
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.get_version()
'5.1.1'

-> Check installed modeules and packegs in your env.
([virtual-env-name])...<base-dir>>>> pip list/pip freeze

-> add your installed modeules and packages inside requirements.txt file
([virtual-env-name])...<base-dir>>>> pip freeze >  requirements.txt

-> install and update modueles and packages from requirements.txt file
([virtual-env-name])...<base-dir>>>> pip install -r requirements.txt

-> create django project
([virtual-env-name])...<base-dir>>>> django-admin startproject [project-name] .

-> create django app's
([virtual-env-name])...<base-dir>>>> python manage.py startapp [app-name] [main-apps-dir]/[app-name]

go to setting.py and add your app name in "INSTALLED_APPS"

Also, change apps name inside [main-apps-dir]/[app-name]/apps.py file

from django.apps import AppConfig
class MasterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '[main-apps-dir].[app-name]'

-> run your django project in your local system
([virtual-env-name])...<base-dir>>>> python manage.py runserver [IP-Address- A.B.C.D]:[port]

-> migrate and makemigration
([virtual-env-name])...<base-dir>>>> python manage.py migrate
([virtual-env-name])...<base-dir>>>> python manage.py makemigrations

-> create superuser account
([virtual-env-name])...<base-dir>>>> python manage.py createsuperuser
Username (leave blank to use '[system-name]'): admin
Email address: admin
Error: Enter a valid email address.
Email address: admin@gmail.com
Password: ********
Password (again): ********
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.


<!--  templates config -->

[main-apps-dir]/[app-name]/
    - templates/
        - [app-name]
            - index.html
            - products.html
            - profile.html

[main-apps-dir]/[app-name]/
    - static/
        - [app-name]
            - CSS
            - JS
            - Fonts
            - Images


form setup

step-1] <form  action="#" method="post" enctype="multipart/form-data">
step-2] {% csrf_token %}
step-3] make sure name attribute in your every Input fields : <input type="email" name="email" />
step-4] <button type="submit"></button>


API's Docs:

API's status_code : https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

LISTAPIS:

POST : Insert new data 
GET : get all data

DETAILAPIS

GET : get specific data 
PUT : update specific data [* required all fields ]
PATCH : update specific data [* partially fields required ]
DELETE : delete specific data


https://<github-username>:<token>@github.com/brijeshpytops/FrostyBites.git