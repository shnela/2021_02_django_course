from django.db import models


class ShortMessageService(models.Model):
    content = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        'customers.Customer',
        on_delete=models.CASCADE,
    )


class Call(models.Model):
    call_date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True)
    customer = models.ForeignKey(
        'customers.Customer',
        on_delete=models.CASCADE,
    )
