# Generated by Django 3.2 on 2021-05-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_portfolioupdate_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioupdate',
            name='seeking',
        ),
        migrations.AlterField(
            model_name='portfolioupdate',
            name='skills',
            field=models.CharField(choices=[('C', 'C'), ('C++', 'C++'), ('PHP', 'PHP'), ('Python', 'Python'), ('Java', 'CJava'), ('CSS', 'CSS'), ('Bootstrap', 'Bootstrap'), ('JavaScript', 'JavaScript'), ('MySql', 'MySql'), ('Oracle', 'Oracle'), ('Postgres', 'Postgres'), ('MongoDB', 'MongoDB'), ('CodeIgniter', 'CodeIgniter'), ('Django', 'Django'), ('Flask', 'Flask'), ('ASP.Net', 'ASP.Net'), ('Android', 'Android'), ('UI/UX', 'UI/UX'), ('Android', 'Android'), ('Photoshop', 'Photoshop'), ('Premiere pro', 'Premiere pro'), ('Drawing', 'Drawing'), ('MS Office', 'MS Office'), ('XCEL', 'XCEL'), ('PowerPoint', 'PowerPoint'), ('Linux', 'Linux'), ('AWS', 'AWS'), ('CCNA', 'CCNA')], max_length=100),
        ),
    ]
