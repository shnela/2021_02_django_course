# Relations

## Serializing relations
In [customers/serializers.py](../battlefield/gsm_provider/customers/serializers.py) add:

```python
class SimpleCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ['call_date', 'duration']
```

## Optimize related object access
[Database access optimization]

### select / prefetch related fields
In [customers/api.py](../battlefield/gsm_provider/customers/api.py) add:
```python
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.prefetch_related('calls_made').all()
    ...
```

### Use managers
In [customers/models.py](../battlefield/gsm_provider/customers/models.py) add:
```python
class CustomerManager(models.Manager):
    def business(self):
        return self.filter(type=Customer.BUSINESS)
```

In shell:
```python
from customers.models import Customer
Customer.objects.business()
```


<!-- links -->
[Serializer relations]: https://www.django-rest-framework.org/api-guide/relations/
[Database access optimization]: https://docs.djangoproject.com/en/3.1/topics/db/optimization/
[Managers]: https://docs.djangoproject.com/en/3.1/topics/db/managers/
