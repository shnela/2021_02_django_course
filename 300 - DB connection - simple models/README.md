# DB connection - simple models

## Create simple `Customer` model
[Django - Models]

Create model in [customers/models.py](../battlefield/gsm_provider/customers/models.py)
```python
class Customer(models.Model):
    username = models.CharField(max_length=128)
```

### Let's now create instance of `Customer` in database


In [Django - shell] run proper [Django - Making queries]:
```bash
python manage.py shell -i ipython
```

In shell:
```python
from customers.models import Customer
Customer(name='some name').save()
```

#### Error 1: register application in settings
Remeber about updating `` in [sm_provider/settings.py](../battlefield/gsm_provider/gsm_provider/settings.py)
```python
INSTALLED_APPS = [
    #...
    'customers',
    #...
]
```

#### Error 2: No database - prepare migrations
[Django - Migrations]

```shell
python manage.py makemigrations
python manage.py migrate
```

### Connect to MySQL database
Update [gsm_provider/settings.py](../battlefield/gsm_provider/gsm_provider/settings.py)

```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': '5432',
    }
}
```

#### Make sure that you use env variables in env
```shell
source ./deployment/variables.env
python manage.py shell -i ipython
```

## Exercises
### Modify `Customer` model
[Django - Model field reference]

1. Make `username` unique
2. Add `type` field:
   * Use `choices` attribute of `CharField`
   * Implement following options of `TYPE_CHOICES`:
     * `Individual`
     * `Business`
    
### Create new app `billings`
And prepare two models for it:
* `ShortMessageService`
    * `content`
    * `send_date`
* `Call`
    * `call_date`
    * `duration`
    

Remember about:
* Registering app in settings
* Creating migrations

### Bonus
[Django - Relationship fields]
Link newly created models to users.
    
<!-- links -->
[Django - Models]: https://docs.djangoproject.com/en/3.1/topics/db/models/
[Django - Making queries]: https://docs.djangoproject.com/en/3.1/topics/db/queries/
[Django - Model field reference]: https://docs.djangoproject.com/en/3.1/ref/models/fields/
[Django - shell]: https://docs.djangoproject.com/en/3.1/ref/django-admin/#shell
[Django - Migrations]: https://docs.djangoproject.com/en/3.1/topics/migrations/
[Django - Relationship fields]: https://docs.djangoproject.com/en/3.1/ref/models/fields/#module-django.db.models.fields.related

