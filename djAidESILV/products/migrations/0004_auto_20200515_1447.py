# Generated by Django 2.2.12 on 2020-05-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200515_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bay_product',
        ),
        migrations.AddField(
            model_name='product',
            name='baby_product',
            field=models.BooleanField(default=False, verbose_name='Produit pour enfant'),
        ),
    ]
