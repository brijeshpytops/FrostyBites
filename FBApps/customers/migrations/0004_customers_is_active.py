# Generated by Django 5.1.1 on 2024-10-08 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]