# Generated by Django 5.0.3 on 2024-05-14 18:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_remove_company_username_company_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
