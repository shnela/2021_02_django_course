# Serializing and Validation

## Make assumption about `Customer.msisdn` field
* [Serializer fields]
* [Custom fields]

In: [customers/serializers.py](../battlefield/gsm_provider/customers/serializers.py)
```python
class PhoneField(serializers.Field):
    def to_representation(self, value):
        return f'+48 {value}'

    def to_internal_value(self, data):
        match_pattern = re.match(r'^+48 \d{3}(-\d{3}){2}$', data)
        if not match_pattern:
            raise ValidationError('Expecting data of format: "XXX-XXX-XXX"')
        return data

class CourseValidator:
    def __init__(self):
        pass

    def __call__(self, value):
        pass
```

### Exercise
#### Test defined field types
1. Do the same using [Serializer fields]
1. Make sure that only business customer numbers starts with 7.
1. Add read only value `Call.end_time`
1. Write some tests


<!-- links -->
[Serializer fields]: https://www.django-rest-framework.org/api-guide/fields/
[Custom fields]: https://www.django-rest-framework.org/api-guide/fields/#custom-fields
[Validators]: https://www.django-rest-framework.org/api-guide/validators/
