from django.db import models


class ShortMessageService(models.Model):
    content = models.TextField()
    send_date = models.DateTimeField()
    sending_party_id = models.ForeignKey(
        'customers.Customer',
        related_name='smses_sent',
        on_delete=models.CASCADE,
    )
    sent_party_id = models.ForeignKey(
        'customers.Customer',
        related_name='smses_received',
        on_delete=models.CASCADE,
    )


class Call(models.Model):
    call_date = models.DateTimeField()
    duration = models.DurationField(null=True)
    caller = models.ForeignKey(
        'customers.Customer',
        related_name='calls_made',
        on_delete=models.CASCADE,
    )
    callee = models.ForeignKey(
        'customers.Customer',
        related_name='calls_received',
        on_delete=models.CASCADE,
    )
