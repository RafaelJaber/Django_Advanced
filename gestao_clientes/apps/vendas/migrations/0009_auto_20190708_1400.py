# Generated by Django 2.0.1 on 2019-07-08 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20190627_2153'),
        ('vendas', '0008_auto_20190701_1048'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('sale', 'product')},
        ),
    ]
