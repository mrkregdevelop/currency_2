# Generated by Django 4.2.2 on 2023-08-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_alter_rate_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='code_name',
            field=models.CharField(default=1, max_length=32, verbose_name='Code name'),
            preserve_default=False,
        ),
    ]