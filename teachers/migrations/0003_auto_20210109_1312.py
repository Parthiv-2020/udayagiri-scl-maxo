# Generated by Django 3.1.5 on 2021-01-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_remove_teacher_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='teacher',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='teacher',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='teacher',
            name='rating',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='teacher',
            name='requests',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='teacher',
            name='salary_annual',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='teacher',
            name='salary_monthly',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='teacher',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
