# Generated by Django 5.1.1 on 2024-10-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='password',
            field=models.CharField(blank=True, default='1234', max_length=255),
        ),
    ]