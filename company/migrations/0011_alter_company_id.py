# Generated by Django 5.0.3 on 2024-05-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_alter_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.UUIDField(default=0, editable=False, primary_key=True, serialize=False),
        ),
    ]