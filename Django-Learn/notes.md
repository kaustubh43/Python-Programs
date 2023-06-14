# Learning Django Framework in Python

## Getting started with a new project
>
> Creating a project:
> Inside your terminal `django-admin startproject smartnotes .`
> We have a directory - 'smartnotes' comprising of
>> __init__.py, asgi.py, settings.py, urls.py, wsgi.py
>
>> ### How to run a server
>>
>> To run a server `python manage.py runserver`

## Creating Apps
>
> To Compartmentalise our project we use Apps:
>
> Apps are smaller sections that have clear boundaries from each other
>
> Command to make an app `django-admin startapp home`
>
> To configure the created app to project we need to modify .\settings.py
>>
 ```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'home',
]
```

>> It is a good practice to separate your apps from the default/native apps.

## Django MVT: Model View Template
>
>The MVT (Model View Template) is a software design pattern. It is a collection of three important components Model View and Template. The Model helps to handle database. It is a data access layer which handles the data.

The Template is a presentation layer which handles User Interface part completely. The View is used to execute the business logic and interact with a model to carry data and renders a template.

## Creating View
>
> Inside our app we will have views.py
>
> We can write a function for starters
>
```
    def home(request):
    return HttpResponse('Hello, World')
```
>
> Now we need to add this in our urls.py like so
>>
>>
```
from django.contrib import admin
from django.urls import path\

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home)
]
```

## Creating Template
>
> It is a common convention to create templates inside the app directory. This is called organisation pattern for Django.
>
> In this case it will be `home\templates\home`
>
> In this directory we will `have welcome.html`
>
> To help us display this welcome we will have to modify views.py in home app
>
```
    def home(request):
    return render(request, 'home/welcome.html', {})
```
>
> Django is using a template framework to render the HTML files. This is called DTL: Django Template Language.
>
> We can use the extra paramter at the end of the function as a way of passing down information
>

> Why modularization is required using apps
>> It is necessary that everything that is required by the app is well contained within that app itself.
>>
>>
>> Earlier we created a dependency for the smartnotes on home app
>>
>> To remove this we need to do some changes
>>> we need to create urls.py in the home app: `home/urls.py`
>>> and write the following code

```from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home)
]
```
>>>
>>> and in smartnotes we need to add a generic format so that the dependency on home app is removed
>>>
>>> To do so we need to write the following code
>>>
>>>
```
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
```

# Django Built in User Management
