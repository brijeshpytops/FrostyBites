# Generated by Django 5.1.1 on 2024-11-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRequests',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('request_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('customer_id', models.CharField(max_length=255)),
                ('messages', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
