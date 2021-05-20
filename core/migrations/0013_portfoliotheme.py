# Generated by Django 3.2 on 2021-05-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_portfolioupdate_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designer', models.CharField(blank=True, max_length=50, null=True)),
                ('designerurl', models.URLField(blank=True, null=True)),
                ('popularity', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]