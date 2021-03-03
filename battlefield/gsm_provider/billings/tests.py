from django.test import TestCase
from model_bakery import baker
from billings.models import Call, ShortMessageService
from customers.models import Customer
from freezegun import freeze_time
from datetime import datetime, timezone, timedelta


class CallTestCase(TestCase):
    def setUp(self):
        baker.make(Call, _quantity=10)

    def test_too_much(self):
        customers = Customer.objects.all()
        self.assertEqual(20, len(customers))


class FreezegunTestCase(TestCase):
    def setUp(self):
        self.sms = baker.make('ShortMessageService',
                              send_date=datetime(2019, 12, 10, tzinfo=timezone.utc),
                              )

    def test_day_ago(self):
        day_ago = datetime.now(tz=timezone.utc) - timedelta(days=1)
        recent_sms = ShortMessageService.objects.filter(send_date__gt=day_ago)
        self.assertFalse(recent_sms.exists())

        some_time = datetime(2019, 12, 10, hour=10, tzinfo=timezone.utc)
        with freeze_time(some_time):
            day_ago = datetime.now(tz=timezone.utc) - timedelta(days=1)
            recent_sms = ShortMessageService.objects.filter(send_date__gt=day_ago)
            self.assertTrue(recent_sms.exists())
