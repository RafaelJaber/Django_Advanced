from django.test import TestCase
from .models import Sale, OrderItem
from gestao_clientes.apps.produtos.models import Product


class SaleTestCase(TestCase):
    def setUp(self):
        self.sale = Sale.objects.create(number="123", discount=10, status='OP')
        self.product = Product.objects.create(description='Product 1', price=10)

    def test_verified_number_of_sales(self):
        """ Verifica o número de vendas """
        assert Sale.objects.all().count() == 1

    def test_value_of_sale(self):
        """ Verifica o valor total da venda """
        OrderItem.objects.create(sale=self.sale, product=self.product, quantities=10, discount=10)
        assert self.sale.value == 80

    def test_discount(self):
        assert self.sale.discount == 10

    def test_item_include_list_items(self):
        item = OrderItem.objects.create(sale=self.sale, product=self.product, quantities=5, discount=10)

        self.assertIn(item, self.sale.orderitem_set.all())

    def test_check_nf_submit(self):
        self.assertFalse(self.sale.nfe_issued)

    def test_check_status(self):
        self.sale.status = 'PC'
        self.sale.save()
        self.assertEqual(self.sale.status, 'PC')
