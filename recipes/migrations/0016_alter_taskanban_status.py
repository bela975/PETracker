# Generated by Django 4.2 on 2023-05-28 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_taskanban_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskanban',
            name='status',
            field=models.CharField(default='to_do', max_length=255),
        ),
    ]