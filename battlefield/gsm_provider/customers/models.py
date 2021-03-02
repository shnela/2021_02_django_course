from django.db import models


class CustomerManager(models.Manager):
    def business(self):
        return self.filter(type=Customer.BUSINESS)


class Customer(models.Model):
    INDIVIDUAL = 'IND'
    BUSINESS = 'BUS'
    TYPE_CHOICES = [
        (INDIVIDUAL, 'Individual'),
        (BUSINESS, 'Business'),
    ]
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=INDIVIDUAL,
    )
    username = models.CharField(max_length=128, unique=True)
    msisdn = models.CharField(max_length=16, unique=True, null=True)
    objects = CustomerManager()

    def __str__(self):
        return f'[{self.id}] {self.username} - {self.type}'
