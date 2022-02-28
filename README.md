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
# Playing With Urls
### Examples 
```
from django.urls import path
from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
```
#### In The Project's url.py --> if request comming with blank path then send it to the <|APPS|>.urls file to done next thing with the url
urls.py # PROJECT
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include('home.urls')),
]
```
#### In the App's urls.py
urls.py # APP
```
from django.urls import path
from home import views

urlpatterns = [
    path('', view=views.index, name = 'home' ),
    path('/about', view=views.about, name='about'),
    path('/contact', view=views.contact, name='contact'),
    path('/services', view=views.services, name='services')
]
```
# In Views.py --> Defining functions which we are call from app's urls.py path('', view=views.index, name = 'home' ), [view=views.index] int views.py file the index function has been use here
```
from django.shortcuts import render

# Create your views here. 
def index(request):
    return render(request=request, template_name='index.html')
    
def about(request):
    return render(request=request, template_name='about.html')

def contact(request):
    return render(request=request, template_name='contact.html')
   
def services(request):
    return render(request=request, template_name='services.html')
```
