from django.core.management.base import BaseCommand
from faker import Faker

from customers.models import Customer

fake = Faker()


class Command(BaseCommand):
    help = 'Initializes Customer model'

    def add_arguments(self, parser):
        parser.add_argument('customers_no', type=int)

    def handle(self, *args, **options):
        customers_to_add = list()
        for _ in range(options['customers_no']):
            customers_to_add.append(
                Customer(username=fake.unique.first_name())
            )
        Customer.objects.bulk_create(customers_to_add)
