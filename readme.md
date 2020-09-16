# Django via Tutorial

## Tutorials

- https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 <sup>Python</sup>
- https://www.youtube.com/watch?v=VuETrwKYLTM&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=87 <sup>Django</sup>
- https://www.youtube.com/playlist?list=PLgCYzUzKIBE9Pi8wtx8g55fExDAPXBsbV <sup>Django REST API</sup>
	- https://www.django-rest-framework.org/tutorial/quickstart/

## Setup

1. Download and install Python and PIP https://www.python.org/downloads/ . Put Python and PIP into PATH. Check with `python --version` & `pip --version` . 
2. Setup a **virtual environment** . Having a virtual environment means that Django configs won't be computer-wide, but per-project.
	* `venv` is a package that comes with Python 3. Python 2 does not contain `venv`.
		*. `python3 -m venv test`
		*. `source test/bin/activate` or `test\Scripts\activate` for Windows
	* `virtualenv` is a tool that allows you to create isolated Python environments, which can be quite helpful when you have different projects with differing requirements. It is a library that offers more functionality than `venv`. ( https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3 )
		*. `pip3 install virtualenv`
		*. `virtualenv -p python3 test`
		*. `source test/bin/activate`
	* mkvirtualenv is command under virtualenvwrapper which is just a wrapper utility around virtualenv that makes it even easier to work with. ( https://stackoverflow.com/questions/44063274/differences-between-mkvirtualenv-and-virtualenv-for-creating-virtual-environment )
		*. `pip install virtualenvwrapper-win  # create the env wrapper`
		*. `mkvirtualenv test                  # create the env`
	* Navigating virtual environments
		* https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/
		* https://stackoverflow.com/questions/990754/how-to-leave-exit-deactivate-a-python-virtualenv
			* If you exited an virtual env and want to re-enter: `workon test`
		* `lsvirtualenv` to list all virtual environments.
	* In my example, I used `virtualenvwrapper-win` and then created a virtual environment called 'test'. 
3. Install Django. `(test) C:\Users\{username}\Documents>pip install django`.
4. `mkdir djangoprojs` & `cd djangoprojs`.
5. Create a project `django-admin startproject tutorial1`.
6. Create an app (an app is like a feature inside a project) `cd tutorial1` & `python manage.py startapp calc`.
7. Take a look of what you have so far by launching server `python manage.py runserver`.

## Notes

- Use `python manage.py help` to show all available commands.
- Django follow MVT pattern. View is like the controller and Template is like the view.

## 1a Hello World

In the newly created calc app, let's just make it say "Hello world" first.

`tutorial1/urls.py`
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),
]
```

`calc/urls.py`
```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

`calc/views.py`
```py
from django.http import HttpResponse

def home(request):
	return HttpResponse("Hello world");	
```

## 1b Hello World with template

Create `templates/home.html`
```html
<h1>Hello world</h1>
```

`tutorial1/settings.py`
```py
import os
# ...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

`calc/views.py`
```py
from django.shortcuts import render

def home(request):
	return render(request, 'home.html');	
```

## 1c Hello World with template with passed data

`templates/home.html`
```html
<h1>Hello {{name}}</h1>
```

`calc/views.py`
```py
from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'name':'someone'});	
```

## 1d Hello World with template with passed data

Create `templates/base.html`
```html
<!DOCTYPE html>
<html>
	<title>Django Tutorial</title>
	<body>

		{% block content %}
		
		{% endblock %}

	</body>
</html>
```

`templates/home.html`
```html
{% extends 'base.html' %}

{% block content %}
<h1>Hello {{name}}</h1>
{% endblock %}
```

## 2a Addition

`templates/home.html`
```html
{% extends 'base.html' %}

{% block content %}
<form action="add">
	<input type="number" name="no1"><br>
	<input type="number" name="no2"><br>
	<input type="submit">
</form> 
{% endblock %}
```

Create `templates/result.html`
```html
{% extends 'base.html' %}

{% block content %}
<h1>Hello {{name}}</h1>

Result: {{result}}
{% endblock %}
```

`calc/urls.py`
```py
urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'), # add this route
]
```

`calc/views.py`
```py
# ...
def add(request):
	no1 = int(request.GET['no1'])
	no2 = int(request.GET['no2'])
	result = no1 + no2

	return render(request, 'result.html', {'result':result});	
```

## 2b Addition (using POST)

`templates/home.html`
```html
{% extends 'base.html' %}

{% block content %}
<form action="add" method="post">
	{% csrf_token %}
	<input type="number" name="no1"><br>
	<input type="number" name="no2"><br>
	<input type="submit">
</form> 
{% endblock %}
```

`calc/views.py`
```py
# ...
def add(request):
	no1 = int(request.POST['no1'])
	no2 = int(request.POST['no2'])
	result = no1 + no2

	return render(request, 'result.html', {'result':result});	
```

## Templating

1. Use existing template: https://colorlib.com/wp/template/travello/

2. `cp travello/index.html templates/travello.html`

3. `tutorial1/urls.py`
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),
    path('travello', include('travello.urls')),
]
```

4. `travello/urls.py`
```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

5. `travello/views.py`
```py
from django.shortcuts import render

def index(request):
	return render(request, "travello.html")
```

But now all the media links are wrong.

### Static files

6. Create a 'static' folder. Copy all the css, js and images into it.

7. Add to `tutorial1/settings.py`
```py
# ...
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
```

8. Then run `python manage.py collectstatic`, an 'assets' folder will be there.

9. Now in `travello.html`, change things like `href="styles/bootstrap4/bootstrap.min.css"` to `href="{% static 'styles/bootstrap4/bootstrap.min.css' %}"`

10. Tell Django to load static files first by putting `{% load static %}` at the top of `travello.html`.

### Send data to the template

11. `travello/models.py`
```py
from django.db import models

class Destination:
	id    : int
	name  : str
	img   : str
	desc  : str
	price : int
	offer : bool
```

12. `travello/views.py`
```py
from django.shortcuts import render
from .models import Destination

def index(request):
	dest1 = Destination()
	dest1.name = 'Mumbai'
	dest1.desc = 'Beautiful City'
	dest1.img = 'destination_3.jpg'
	dest1.price = 700
	dest1.offer = True

	dest2 = Destination()
	dest2.name = 'Mumbai'
	dest2.desc = 'Beautiful City'
	dest2.img = 'destination_3.jpg'
	dest2.price = 700
	dest2.offer = False

	dests = [dest1,dest2]
	
	return render(request, "travello.html", {'dests': dests})
```

13. `templates/travello.html`
```html
{% load static %}
{% static "images" as baseUrl %} <!-- Add this line -->

<!-- ... -->

<!-- Alter Destination section as below -->
{% for dest in dests %}
<!-- Destination -->
<div class="destination item">
	<div class="destination_image">
		<img src="{{baseUrl}}/{{dest.img}}" alt="">
		{% if dest.offer %}
		<div class="spec_offer text-center"><a href="#">Special Offer</a></div>
		{% endif %}
	</div>
	<div class="destination_content">
		<div class="destination_title"><a href="destinations.html">{{dest.name}}</a></div>
		<div class="destination_subtitle"><p>{{dest.desc}}</p></div>
		<div class="destination_price">From ${{dest.price}}</div>
	</div>
</div>
{% endfor %}
```

## Adding DB

1. Download and install:

![](https://github.com/Ruslan-Aliyev/Django-and-Django-RESTful-API-Lesson/blob/master/Illustrations/postgresql.PNG)

2. Install DB adapter: `pip install psycopg2` 

3. `tutorial1/settings.py`
```py
INSTALLED_APPS = [
    'travello.apps.TravelloConfig',
    # ...
]

# ...

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoTut1',
        'USER': 'postgres',
        'PASSWORD': '***',
        'HOST': 'localhost',
    }
}
```

4. Alter `travello/models.py` to
```py
class Destination(models.Model):
	#id: int
	name  = models.CharField(max_length=100)
	img   = models.ImageField(upload_to='pics')
	desc  = models.TextField()
	price = models.IntegerField()
	offer = models.BooleanField(default=False)
```

Refer to: https://docs.djangoproject.com/en/3.1/ref/models/fields/

5. When using ImageField, need to `pip install Pillow`

6. `python manage.py makemigrations` - new migration file is created in `travello/migrations/` .

7. `python manage.py sqlmigrate travello 0001` - will let you see the SQL code that would execute.

8. `python manage.py migrate` - actually migrates. You'll see the results in the DB. PgAdmin: Servers -> PostgreSQL -> Databases -> djangoTut1 -> schemas -> public -> Tables.

### Backend admin

We want to insert new entries via the backend.

Django gives an inbuilt admin backside: http://localhost:8000/admin

9. But need to create super-admin by: `python manage.py createsuperuser`

10. `travello/admin.py`
```py
from django.contrib import admin
from .models import Destination

admin.site.register(Destination)
```

![](https://github.com/Ruslan-Aliyev/Django-and-Django-RESTful-API-Lesson/blob/master/Illustrations/backend.PNG)

11. Add to `tutorial1/settings.py`
```py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

12. Edit `tutorial1/urls.py`
```py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings            # Add this
from django.conf.urls.static import static  # Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),
    path('travello', include('travello.urls')),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Add this
```

13. Add some entries via the backend

Note: Recall `pics` folder from step 4. Uploaded images will end up in `media/pics/`.

14. Edit `travello/views.py`
```py
def index(request):
	dests = Destination.objects.all()
	return render(request, "travello.html", {'dests': dests})
```

15. But now the image links are out of place. 

So now in `templates/travello.py`, replace `<img src="{{baseUrl}}/{{dest.img}}" alt="">` with `<img src="{{dest.img.url}}" alt="">`

## User accounts

1. `python manage.py startapp accounts`

2. `accounts/urls.py`
```py
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
```

3. Do `accounts/views.py` 

4. Add `templates/register.html` & `templates/login.html`

We are utilizing the inbuilt `auth_user` table, so make the registration form fields accordingly.

5. Add `path('accounts/', include('accounts.urls'))` to `tutorial1/urls.py`

6. Add to `templates/travello.html`
```html
{% if user.is_authenticated %}
<li>Hello, {{user.first_name}}</li>
<li><a href="accounts/logout">Logout</a></li>
{% else %}
<li><a href="accounts/register">Register</a></li>
<li><a href="accounts/login">Login</a></li>
{% endif %}
```

## RESTful API

Intention is to add API to the `travello` app.

1. `pip install djangorestframework`

2. `tutorial1/settings.py`
```py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

3. `tutorial1/urls.py`
```py
# ...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),
    path('travello', include('travello.urls')),
    path('accounts/', include('accounts.urls')),
    
    # REST
    path('api/travello', include('travello.api.urls', 'travello_api')), # Add this
]
```

4. Create `travello/api/serializers.py`
```py
from rest_framework import serializers
from travello.models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'name', 'img', 'desc', 'price', 'offer']
```

NOTE: Don't forget to put `__init__.py` into `api` folder when you create the `api` folder.

5. `travello/api/urls.py`

Just do the GETs for now:

```py
from django.urls import path
from travello.api.views import (api_index, api_dest)

app_name = 'travello'

urlpatterns = [
    path('/', api_index, name='index'),
    path('/<id>/', api_dest, name='dest'),
]
```

6. `travello/api/views.py`
```py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from travello.models import Destination
from travello.api.serializers import DestinationSerializer

@api_view(['GET'])
def api_index(request):
	dests = Destination.objects.all()
	serializer = DestinationSerializer(dests, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def api_dest(request, id):

	try:
		dest = Destination.objects.get(id=id)
	except Destination.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = DestinationSerializer(dest)
	return Response(serializer.data)
```

7. See from browser: `http://localhost:8000/api/travello/` & `http://localhost:8000/api/travello/1/`
