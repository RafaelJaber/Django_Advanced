from django.db import models
from gestao_clientes.apps.clientes.models import Person
from gestao_clientes.apps.produtos.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum, F, FloatField, Max
from .managers import SaleManager


class Sale(models.Model):
    number = models.CharField(max_length=7, verbose_name='Número')
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total R$', blank=True, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Desconto R$', default=0)
    taxes = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Impostos R$', default=0)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Cliente')
    nfe_issued = models.BooleanField(default=False, blank=True)

    objects = SaleManager()

    def __str__(self):
        return self.number

    def calculate_total(self):
        total = self.orderitem_set.all().aggregate(
            total_order=Sum((F('quantities') * F('product__price')) - F('discount'), output_field=FloatField())
        )['total_order'] or 0
        total = total - float(self.taxes) - float(self.discount)

        Sale.objects.filter(id=self.id).update(value=total)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering = ['number']
        permissions = (
            ('setar_nfe', 'Usuário pode alterar parametro NF-e'),
            ('ver_dash', 'Usuário que podem acessar a dashboard'),
        )


class OrderItem(models.Model):

    sale = models.ForeignKey(Sale, verbose_name='Venda', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Produto', on_delete=models.CASCADE)
    quantities = models.FloatField(verbose_name='Quantidade', default=1)
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Desconto', default=0)

    def __str__(self):
        return self.sale.number + ' - ' + self.product.description

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'


@receiver(post_save, sender=OrderItem)
def update_sale_total(sender, instance, **kwargs):
    instance.sale.calculate_total()


@receiver(post_save, sender=Sale)
def update_sale_total_2(sender, instance, **kwargs):
    instance.calculate_total()
