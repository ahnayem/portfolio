# Generated by Django 3.2 on 2021-05-09 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_portfolioupdate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioupdate',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]