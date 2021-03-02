from django.contrib.auth.models import User
from django.test import TestCase
from customers.models import Customer
from rest_framework.test import APIClient


class CustomerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='someone', password='pass')

    def test_create(self):
        self.client.force_authenticate(user=self.user)
        request = self.client.post('/api/customers/', {'username': 'Ada'})
        self.assertEqual(request.status_code, 201)

        ada = Customer.objects.first()
        self.assertEqual(ada.username, 'Ada')
