# Generated by Django 3.2 on 2021-05-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20210513_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioupdate',
            name='skills',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]