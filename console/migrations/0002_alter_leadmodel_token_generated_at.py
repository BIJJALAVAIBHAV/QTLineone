# Generated by Django 4.1 on 2024-04-26 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadmodel',
            name='token_generated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 9, 14, 39, 507001)),
        ),
    ]