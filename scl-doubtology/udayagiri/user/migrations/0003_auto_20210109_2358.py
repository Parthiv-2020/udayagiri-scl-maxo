# Generated by Django 3.1.5 on 2021-01-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210105_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/profile_pics/default.png', upload_to='media/profile_pics/%Y/%m/'),
        ),
    ]
