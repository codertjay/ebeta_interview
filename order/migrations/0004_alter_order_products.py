# Generated by Django 4.0.6 on 2022-07-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_order_state_alter_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, to='order.orderproduct'),
        ),
    ]
