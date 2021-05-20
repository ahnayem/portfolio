# Generated by Django 3.2 on 2021-05-10 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210510_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designer', models.CharField(blank=True, max_length=50, null=True)),
                ('designerurl', models.URLField(blank=True, null=True)),
                ('popularity', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='PortfolioTheme',
        ),
    ]