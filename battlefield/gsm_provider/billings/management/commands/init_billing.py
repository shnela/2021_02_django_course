from datetime import timedelta
from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from billings.models import Call, ShortMessageService
from customers.models import Customer

fake = Faker()


class Command(BaseCommand):
    help = 'Initializes Customer model'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        sms_to_add = list()
        call_to_add = list()
        for customer in Customer.objects.all():
            for _ in range(options['n']):
                sms_to_add.append(
                    ShortMessageService(content=fake.text(),
                                        customer=customer)
                )
                call_to_add.append(
                    Call(duration=timedelta(seconds=randint(10, 1000)),
                         customer=customer)
                )
        ShortMessageService.objects.bulk_create(sms_to_add)
        Call.objects.bulk_create(call_to_add)
