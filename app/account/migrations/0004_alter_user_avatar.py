# Generated by Django 4.2.2 on 2023-08-09 17:41

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, default=None, null=True, upload_to=account.models.avatar_path, verbose_name='Avatar'),
        ),
    ]
