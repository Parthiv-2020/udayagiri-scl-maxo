# Generated by Django 3.1.5 on 2021-01-07 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='rate',
        ),
    ]