# Generated by Django 3.2 on 2021-05-10 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_portfoliotheme_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliotheme',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
