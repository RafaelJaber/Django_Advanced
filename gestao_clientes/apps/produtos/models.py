from django.db import models
from gestao_clientes.apps.vendas.models import Sale


class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['description']


class OrderItem(models.Model):
    sale = models.ForeignKey(Sale, verbose_name='Venda', on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Product, verbose_name='Produto', on_delete=models.CASCADE)
    quantities = models.FloatField(verbose_name='Quantidade')
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Desconto')

    def __str__(self):
        return self.sale.number + ' - ' + self.product.description

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'
