# Generated by Django 5.0.3 on 2024-05-18 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_alter_employee_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='cv',
        ),
    ]