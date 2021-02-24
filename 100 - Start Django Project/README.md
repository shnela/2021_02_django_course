# Start Django App
[Django vs Rails]

## Prepare virtualenv
```bash
# Create new python environment in ~/.envs/2021_02_django_course
python3 -m venv ~/.envs/2021_02_django_course
# Activate environment
source ~/.envs/2021_02_django_course/bin/activate

# install dependencies
pip install django
# check what's installed
pip freeze
```

## Create Django Project
[Django - Creating a project]

```bash
# in 2021_02_django_course/battlefield
cd 2021_02_django_course/battlefield
django-admin startproject gsm_provider
```

Analyze files created in `battlefield/gsm_provider` and `battlefield/gsm_provider/gsm_provider` directories.

## Runserver
[Django - The development server]

```
# in battlefield/gsm_provider
python manage.py runserver
```

And visit http://127.0.0.1:8000/

> Automatic reloading of runserver 
> 
> The development server automatically reloads Python code for each request as needed.
> You don’t need to restart the server for code changes to take effect.
> However, some actions like adding files don’t trigger a restart,
> so you’ll have to restart the server in these cases.

## Configure pyCharm

To set custom environment used by pyCharm go to:
```
File | Settings | Project: 2021_02_django_course | Python Interpreter
```
`Right Click on gear` &rarr; `Add...` &rarr; `Existing environment` &rarr; `Path to python executable`

### Mark Django root directory as source
[pyCharm - Configuring Project Structure]

`Right Click on 'battlefield/gsm_provider'` &rarr; `Mark directory as...` &rarr; `Sources root`

Now pyCharm will be able to successfully resolve absolute imports.

## Create new App
```bash
# in battlefield/gsm_provider
python manage.py startapp customers
```

We have new directory: `battlefield/gsm_provider/customers`

> Projects vs. apps
> 
> What’s the difference between a project and an app?
> An app is a Web application that does something – e.g.,
> a Weblog system, a database of public records or a small poll app.
> A project is a collection of configuration and apps for a particular website.
> A project can contain multiple apps. An app can be in multiple projects.

### Views
[Django - Writing views]

Update [customers/views.py](../battlefield/gsm_provider/customers/views.py) with:
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("""
                        <h1>Hi there.</h1>
                        <a href='https://www.youtube.com/watch?v=4ctK1aoWuqY'>Schwifty response</a>
                        """)

```

### Urls
[Django - URL dispatcher]

Update [customers/urls.py](../battlefield/gsm_provider/customers/urls.py) with:
```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

```

_File `customers/urls.py` wasn't created automatically, you have to create it on your own._


And inform core application about changes [gsm_provider/urls.py](../battlefield/gsm_provider/gsm_provider/urls.py).  
Add following line to `urlpatterns`.
```python
    path('customers/', include('customers.urls')),
```

### Ready! [Show Me What You Got]
Visit: http://127.0.0.1:8000/customers/

## Run project on pyCharm
[Create and edit run/debug configurations]

Click on `Add Configuration` on top right corner &rarr; + &rarr; `Python`

### Update run configuration
* `Script path:` `../battlefield/gsm_provider/manage.py`
* `Parameters:` `runserver`
* `Working directory`: `../battlefield/gsm_provider`

<!-- urls -->
[Django vs Rails]: https://stackshare.io/stackups/django-vs-rails
[Django - Creating a project]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-a-project
[Django - The development server]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/#the-development-server
[pyCharm - Configuring Project Structure]: https://www.jetbrains.com/help/pycharm/configuring-project-structure.html
[Django - Writing views]: https://docs.djangoproject.com/en/3.1/topics/http/views/
[Django - URL dispatcher]: https://docs.djangoproject.com/en/3.1/topics/http/urls/
[Show Me What You Got]: https://www.youtube.com/watch?v=m1fZ7Ap6ebs
[Create and edit run/debug configurations]: https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html
