# Generated by Django 2.2.12 on 2020-05-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_userprofile_stripe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bebes',
            field=models.IntegerField(default=0, verbose_name="nombre d'enfants de moins de 4 ans"),
        ),
    ]
