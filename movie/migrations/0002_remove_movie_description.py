# Generated by Django 3.1.5 on 2021-01-25 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
    ]
