# Generated by Django 2.2.5 on 2021-04-07 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210407_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='offer_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
