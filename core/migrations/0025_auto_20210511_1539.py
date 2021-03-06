# Generated by Django 3.2 on 2021-05-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_portfolioupdate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioupdate',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolioupdate',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioupdate',
            name='clg_group',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioupdate',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioupdate',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioupdate',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioupdate',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioupdate',
            name='github',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioupdate',
            name='skills',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioupdate',
            name='uni_subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
