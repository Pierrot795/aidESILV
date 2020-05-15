# Generated by Django 2.2.12 on 2020-05-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bay_product',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('A', 'Alimentation'), ('P', 'Pharmacie'), ('Q', 'Quotidien'), ('NA', 'Non-attribué')], default='NA', max_length=2, verbose_name='Catégorie'),
        ),
    ]