# Generated by Django 3.2 on 2021-05-13 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20210512_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='html',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]