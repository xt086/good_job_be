# Generated by Django 5.0.3 on 2024-05-14 18:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]