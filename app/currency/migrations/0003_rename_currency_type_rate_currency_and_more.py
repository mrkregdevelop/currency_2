# Generated by Django 4.2.2 on 2023-06-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_rate_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='currency_type',
            new_name='currency',
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
