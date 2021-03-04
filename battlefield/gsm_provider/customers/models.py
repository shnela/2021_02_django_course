from django.db import models


class BusinessManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Customer.BUSINESS)


class IndividualManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Customer.INDIVIDUAL)


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
    business = BusinessManager()
    individuals = IndividualManager()

    def __str__(self):
        return f'[{self.id}] {self.username} - {self.type}'
