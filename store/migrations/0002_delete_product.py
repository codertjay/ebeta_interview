# Generated by Django 4.0.6 on 2022-07-28 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderproduct_product'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]