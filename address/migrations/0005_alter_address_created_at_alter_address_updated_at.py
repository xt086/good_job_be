# Generated by Django 5.0.3 on 2024-05-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_address_created_at_address_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
