# Generated by Django 2.0.1 on 2019-06-28 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['description'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]