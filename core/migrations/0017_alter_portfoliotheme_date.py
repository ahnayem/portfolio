# Generated by Django 3.2 on 2021-05-10 11:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_rename_skills_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliotheme',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]