from django.test import TestCase
from customers.models import Customer
from rest_framework.test import APIClient, APIRequestFactory


class CustomerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create(self):
        request = self.client.post('/api/customers/', {'username': 'Ada'})
        self.assertEqual(request.status_code, 201)

        ada = Customer.objects.first()
        self.assertEqual(ada.username, 'Ada')
