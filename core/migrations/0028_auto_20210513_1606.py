# Generated by Django 3.2 on 2021-05-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_theme_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioupdate',
            name='uniM',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolioupdate',
            name='uniM_passing',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='portfolioupdate',
            name='uniM_result',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='portfolioupdate',
            name='uniM_subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
