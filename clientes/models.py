from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Nome')
    last_name = models.CharField(max_length=30, verbose_name='Sobrenome')
    age = models.IntegerField(verbose_name='Idade')
    salary = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Salário')
    bio = models.TextField(verbose_name='Biográfia')
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True, verbose_name='Foto')
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Documento')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['first_name']


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao


class Venda(models.Model):
    numero = models.CharField(max_length=7, verbose_name='Número')
    valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total R$')
    desconto = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Desconto R$')
    impostos = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Impostos R$')
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Cliente')
    produtos = models.ManyToManyField(Produto, blank=True, verbose_name='Produtos')
    nfe_emitida = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.numero

    def get_total_sale(self):
        total = 0
        for product in self.produtos.all():
            total += product.preco
        total = total - self.desconto - self.impostos
        return total

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering = ['numero']


@receiver(m2m_changed, sender=Venda.produtos.through)
def update_sale_total(sender, instance, **kwargs):
    instance.valor = instance.get_total_sale()
    instance.save()
