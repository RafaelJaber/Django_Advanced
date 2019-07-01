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
        permissions = (
            ('list_clients', 'Usuário que pode ver a lista de clientes'),
        )


