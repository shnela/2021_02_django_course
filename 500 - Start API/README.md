# Start API

## Some basics are done
1. [customers/api.py](../battlefield/gsm_provider/customers/api.py)
1. [customers/api_urls.py](../battlefield/gsm_provider/customers/api_urls.py)
1. [gsm_provider/urls.py](../battlefield/gsm_provider/gsm_provider/urls.py)

Visit: http://127.0.0.1:8000/api/customers/

### TemplateDoesNotExist Exception:
[DRF - installation]

Update:
 [gsm_provider/settings.py](../battlefield/gsm_provider/gsm_provider/settings.py)
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    # ...
]
```

Visit:
* <http://127.0.0.1:8000/api/customers/>
* <http://127.0.0.1:8000/api/customers/1/>

## Serialize our model
[DRF - simple serialization]

Add serializer to [customers/serializers.py](../battlefield/gsm_provider/customers/serializers.py)
```python
class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    type = serializers.ChoiceField(choices=Customer.TYPE_CHOICES,
                                   required=False, allow_blank=True)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance

```

### It's time to use `CustomerSerializer`

```python
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)
```

For both: `customer_list` and `customer_list`.

### Let's implement [CRUD]:
[Writing regular Django views using our Serializer]

**Do not use `JSONParser`, just past `response.data` to `CustomerSerializer`**

Use:
```python
if request.method == 'GET':
    ...
elif request.method == 'POST':
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
```

Test 'POST':
```
{
    "username": "New user",
    "type": "IND"
}
```

For both: `customer_list`.

**What’s the Difference between PUT vs PATCH?**

<!-- links -->
[DRF - installation]: https://www.django-rest-framework.org/?q=collectstatic#installation
[DRF - simple serialization]: https://www.django-rest-framework.org/tutorial/1-serialization/#creating-a-serializer-class
[CRUD]: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
[Writing regular Django views using our Serializer]: https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer
[DRF - ModelSerializer]: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer


