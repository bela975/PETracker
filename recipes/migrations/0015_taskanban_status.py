# Generated by Django 4.2 on 2023-05-28 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_taskanban'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskanban',
            name='status',
            field=models.CharField(default=0, max_length=255),
        ),
    ]