from django.test import TestCase
from customers.models import Customer


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username='Alice')
        Customer.objects.create(username='Bob')
        Customer.objects.create(username='Charlie')

    def test_number_of_elements(self):
        customers = Customer.objects.all()
        self.assertEqual(3, len(customers))

    def test_filter(self):
        bob = Customer.objects.filter(username__startswith='B').first()
        self.assertEqual(bob.username, 'Bob')
        nobody = Customer.objects.filter(username__startswith='D').first()
        self.assertIsNone(nobody)

    def test_delete(self):
        customers = Customer.objects
        Customer.objects.first().delete()
        self.assertEqual(2, len(customers.all()))
        Customer.objects.all().delete()
        self.assertEqual(0, len(customers.all()))
