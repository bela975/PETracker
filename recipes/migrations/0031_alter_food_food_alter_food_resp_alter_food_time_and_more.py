# Generated by Django 4.2.2 on 2023-06-08 03:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0030_alter_medicine_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food',
            field=models.CharField(default='exemplo', max_length=50),
        ),
        migrations.AlterField(
            model_name='food',
            name='resp',
            field=models.CharField(default='exemplo', max_length=50),
        ),
        migrations.AlterField(
            model_name='food',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=50),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=50),
        ),
    ]
