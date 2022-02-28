# Create Project ==> open terminal where you want to create project 
##### django-admin startproject PROJET_NAME
``` 
django-admin startproject users
```
```
cd users
```
# migrations and migrate
##### 1. makemigrations
```
python manage.py makemigrations
```
##### 2. migrate
```
python manage.py migrate
```
## run server
```
python manage.py runserver
```
# Create an app as name home
```
python manage.py startapp home
```

# Create Super User
```
python manage.py createsuperuser
```
```
Username (leave blank to use 'root'): ENTER_USERNAME_TO_SET
Email address: ENTER_USERNAME
Password:
Password (again):
```
# Register App
#### settings.py

# go to <APP_FOLDER> copy the class name from apps.py
```
from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
```
### ADD THIS LINE INTO INSTALLED_APPS
#### <APP_NAME>.apps.HomeConfig'
```
'home.apps.HomeConfig'
```
```
# Application definition
INSTALLED_APPS = [
    .
    .
    .
    .
    'home.apps.HomeConfig'
]
```

# SETTING STATIC DIRECTORY AND TEMPLATES DIRECTORY

Make sure that django.contrib.staticfiles is included in your INSTALLED_APPS.

In your settings file, define STATIC_URL, for example:

setting.py
```
STATIC_URL = 'static/'
```
setting.py
```
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]
```
# Overriding from the project’s templates directory

settings.py
```
TEMPLATES = [
    {
        ...,
        'DIRS': [BASE_DIR / "templates"],
        ...
    },
]
```

# allowed host
settings.py
```
ALLOWED_HOSTS = ['mydomaimname.com','127.0.0.1', 'localhost']
```