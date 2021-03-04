from datetime import timedelta, timezone
from random import randint, sample

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
        customers = list(Customer.objects.all())
        for _ in range(options['n'] * len(customers)):
            from_c, to_c = sample(customers, 2)
            sms_to_add.append(
                ShortMessageService(send_date=fake.date_time_between(start_date='-2y',
                                                                     tzinfo=timezone.utc),
                                    content=fake.text(),
                                    sending_party=from_c,
                                    sent_party=to_c)
            )
            call_to_add.append(
                Call(call_date=fake.date_time_between(start_date='-2y',
                                                      tzinfo=timezone.utc),
                     duration=timedelta(seconds=randint(10, 1000)),
                     caller=from_c,
                     callee=to_c)
            )
        ShortMessageService.objects.bulk_create(sms_to_add)
        Call.objects.bulk_create(call_to_add)
