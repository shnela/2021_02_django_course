from django.db import models


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

    def __str__(self):
        return f'[{self.id}] {self.username} - {self.type}'
