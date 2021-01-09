from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField


class Teacher(models.Model):

    subject_choice = (
        ('English Language Arts', 'English Language Arts'),
        ('Art / Music / Theater', 'Art / Music / Theater'),
        ('Social Sciences', 'Social Sciences'),
        ('Mathematics', 'Mathematics'),
        ('Science', 'Science'),
        ('World Language', 'World Language'),
        ('Professional Career', 'Professional Career'),
        ('Multiple Subjects', 'Multiple Subjects'),
        ('Other', 'Other')
    )


    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m/')
    country = CountryField()
    subject = models.CharField(choices=subject_choice, max_length=255)
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    twitter_url = models.CharField(max_length=400, blank=True)
    linkedin_url = models.CharField(max_length=400, blank=True)
    facebook_url = models.CharField(max_length=400, blank=True)
    instagram_url = models.CharField(max_length=400, blank=True)
    salary_monthly = models.CharField(max_length=300, blank=True)
    salary_annual = models.CharField(max_length=300, blank=True)
    rating = models.CharField(max_length=300, blank=True)
    requests = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name
    
    