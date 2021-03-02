# DB connection - generating random models

## Django admin
[The Django admin site]

Actually... What [customers/admin.py](../battlefield/gsm_provider/customers/admin.py)
file is for?!

Try this:
```python
from django.contrib import admin
from customers.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
```

Visit: http://127.0.0.1:8000/admin/

### Authorization required...
[The Django admin site]

Create superuser:
```shell
python manage.py createsuperuser --username=admin
```

**Now log in**.

### Let's play with a layout:
Add
```python
list_display = ('type', 'username')
```

### Exercise
1. Add Admin views for remaining models:
    * `ShortMessageService`
    * `Call`
1. For above models implement and use `customer_display` to nicely display user with name
1. Add customizable `send_date` and `call_date` in form.


## Install DjangoDebugToolbar
[Django Debug Toolbar installation]

```shell
pip install django-debug-toolbar
```

Update:
* [gsm_provider/settings.py](../battlefield/gsm_provider/gsm_provider/settings.py)
  `INSTALLED_APPS`, `STATIC_URL`, `MIDDLEWARE` and `INTERNAL_IPS`
* [gsm_provider/urls.py](../battlefield/gsm_provider/gsm_provider/urls.py)

Now DDT is available in admin page. 

## Custom commands
[django-admin and manage.py]
[Writing custom django-admin commands]
[Use bulk methods]

Look at
[customers/management/commands/init_customers.py](../battlefield/gsm_provider/customers/management/commands/init_customers.py)

Then:
```bash
python manage.py init_customers -h
python manage.py init_customers 
```

### Exercise
Create `init_sms_and_calls` in `billing` app in
`billings/management/commands/init_billing.py`.

Command should generate `n` `ShortMessageService` and `Call` for every user.

Tips:
* You can access all customers with `Customer.objects.all()`
* Use `random.randint` and [Python - timedelta] for generating `Call.duration`

## Performance problems on Admin page?
[ModelAdmin.list_select_related]

Add:
```list_select_related = ('customer',)```
to both `ShortMessageServiceAdmin` and `CallAdmin`.

<!-- links -->
[The Django admin site]: https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
[Using the Django authentication system]: https://docs.djangoproject.com/en/3.1/topics/auth/default/
[Django Debug Toolbar installation]: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
[django-admin and manage.py]: https://docs.djangoproject.com/en/3.1/ref/django-admin/
[Writing custom django-admin commands]: https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/
[Use bulk methods]: https://docs.djangoproject.com/en/3.1/topics/db/optimization/#use-bulk-methods
[Python - timedelta]: https://docs.python.org/3/library/datetime.html#datetime.timedelta
[ModelAdmin.list_select_related]: https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_select_related
