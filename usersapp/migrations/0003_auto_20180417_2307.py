# Generated by Django 2.0.4 on 2018-04-17 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0002_auto_20180417_2242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipesuser',
            options={'ordering': ['user_id', 'username']},
        ),
    ]
