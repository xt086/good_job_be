# Generated by Django 5.0.3 on 2024-05-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_alter_employee_id_alter_employee_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=0, editable=False, primary_key=True, serialize=False),
        ),
    ]
