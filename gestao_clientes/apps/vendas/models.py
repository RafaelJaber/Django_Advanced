from django.db import models
from gestao_clientes.apps.clientes.models import Person
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Sale(models.Model):
    number = models.CharField(max_length=7, verbose_name='Número')
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total R$', blank=True, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Desconto R$')
    taxes = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Impostos R$')
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Cliente')
    nfe_issued = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering = ['number']


#@receiver(m2m_changed, sender=Sale.item.)
def update_sale_total(sender, instance, **kwargs):
    instance.valor = instance.get_total_sale()
    instance.save()
