# Generated by Django 3.1.6 on 2021-02-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210125_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update',
            field=models.BooleanField(default=False, max_length=10),
        ),
    ]