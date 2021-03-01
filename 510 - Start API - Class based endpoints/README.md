# Start API - Class based endpoints


## New model layout
**Drop all tables from db**
* [customers/models.py](../battlefield/gsm_provider/customers/models.py)
* [customers/billing.py](../battlefield/gsm_provider/billing/models.py)

[ForeignKey arguments]


## [Class-based Views]
[Don't repeat yourself]

File: [customers/api.py](../battlefield/gsm_provider/customers/api.py)

## Exercise:

### Prepare `APIView` classes
Prepare class views:
* `class CustomerList(APIView):`
* `class CustomerDetail(APIView):`

Hint:
* Just replace if blocks with `get`, `post` etc functions.
* Remember about url dispatcher change: `CustomerList.as_view()` in
[customers/api_urls.py](../battlefield/gsm_provider/customers/api_urls.py)
  
### Mixins workout
Create `class TimestampMixin` for classes, define it in [utils/model_mixins.py](../battlefield/gsm_provider/utils/model_mixins.py)

It should contain two  fields: `created_at`, `updated_at` of type `DateTimeField`.
Use `auto_add` and `auto_now_add`.

Add mixins as parent class to all models and migrate.

### Make more sense of 

<!-- links -->
[Class-based Views]: https://www.django-rest-framework.org/tutorial/3-class-based-views/#tutorial-3-class-based-views
[Don't repeat yourself]: https://en.wikipedia.org/wiki/Don't_repeat_yourself
[ForeignKey arguments]: https://docs.djangoproject.com/en/3.1/ref/models/fields/#arguments

