# Generated by Django 4.2.2 on 2023-06-08 02:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0029_alter_medicine_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now, max_length=50),
        ),
    ]