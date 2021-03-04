# General

## Start
Init database data according to: 300 - DB connection - simple models/README.md

You can reset database with (`django_extensions`):
```shell
python manage.py reset_db
```

And initialize database using:
```shell
python manage.py initialize_customers 10
python manage.py initialize_billing 10
```

## Exercises
### Object manager
https://docs.djangoproject.com/en/3.1/topics/db/managers/

Add `IndividualManager` manager to `Customer` model and use it for implementing:
http://127.0.0.1:8000/api/individuals/
and
http://127.0.0.1:8000/api/individuals/<id>/

### Aggregation / annotation
https://docs.djangoproject.com/en/3.1/topics/db/aggregation/

Optimize counting related calls and send messages by
annotating queryset in `CustomerList`.

Add number of send/received messages.

### Select related
https://docs.djangoproject.com/en/3.1/ref/models/querysets/#select-related

Optimize access to:
http://127.0.0.1:8000/api/sms/
and
http://127.0.0.1:8000/api/individuals/

Use `select_related` to decrease number SQL queries.

### Pagination
https://www.django-rest-framework.org/api-guide/fields/

Add pagination to project, and set it to 10 elements per page.

Look how it works  in:
http://127.0.0.1:8000/api/sms/
and
http://127.0.0.1:8000/api/calls/

### Validation
https://www.django-rest-framework.org/api-guide/fields/#custom-fields

Write custom serializer `PhoneField` which will:
* requre data in format r'^\+48 (\d{3}(-\d{3}){2})$'
* but saves number in database without +48 prefix
* always renders json with additional +48 prefix

And use it in `DetailCustomerSerializer`.

Make sure that 800 prefixes are reserved for business customers only.

Override `DetailCustomerSerializer.run_validators`

### Display related calls and sms
In `Customer Detail`

You can use related serializers like in `CallSerializer` and `CallSerializer`.

Optimize db access - avoid duplicated queries.

### Add billing per user
Add endpoints:
127.0.0.1:8000/api/business/<id>/billing/<10-2020:date>/

Which will display only calls and sms from given month.
Use model manager.

