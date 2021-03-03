from django.db import models


class ShortMessageService(models.Model):
    send_date = models.DateTimeField()
    content = models.TextField()


class Call(models.Model):
    call_date = models.DateTimeField()
    duration = models.DurationField(null=True)
