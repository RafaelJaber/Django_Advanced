from django.test import TestCase
from .models import Sale


class SaleTestCase(TestCase):
    def setUp(self):
        Sale.objects.create(number="123")

    def test_verified_number_of_sales(self):
        assert Sale.objects.all().count() >= 1
