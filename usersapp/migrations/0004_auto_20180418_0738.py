# Generated by Django 2.0.4 on 2018-04-18 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0003_auto_20180417_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipesuser',
            name='nickname',
            field=models.CharField(max_length=50, unique=True, verbose_name='никнейм'),
        ),
    ]
