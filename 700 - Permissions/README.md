# [Authentication & Permissions]

## Let's use curl
```shell
curl -X POST -H "Content-Type: application/json" -d '{"username":"abc"}' http://127.0.0.1:8000/api/customers/
```

### Secure Client classes
Add
```python
permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```
to customer endpoints.

#### Now we have to authorize
We have
```python
path('api-auth/', include('rest_framework.urls')),
``` 
in [gsm_provider/urls.py](../battlefield/gsm_provider/gsm_provider/urls.py)

##### Curl
```shell
curl -X POST  -u admin:admin  -H "Content-Type: application/json" -d '{"username":"abc"}' http://127.0.0.1:8000/api/customers/
```

##### Fix tests
Use `force_authenticate` and `django.contrib.auth.models.User`.

### User model
https://learndjango.com/tutorials/django-custom-user-model

<!-- links -->
[Authentication & Permissions]: https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
[Forcing authentication]: https://www.django-rest-framework.org/api-guide/testing/#forcing-authentication



