# Generated by Django 5.1.1 on 2024-10-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]