from django.db import models
from django.contrib.auth.models import User

ROLE = (
    ('Teacher', 'Teacher'),
    ('Student', 'Student')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/profile_pics/%Y/%m/')
