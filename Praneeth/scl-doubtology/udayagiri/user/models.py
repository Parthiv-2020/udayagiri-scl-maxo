from django.db import models
from django.contrib.auth.models import User

ROLE = (
    ('Teacher', 'Teacher'),
    ('Student', 'Student')
)

class Role(models.Model):
    role = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.role}'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/profile_pics/%Y/%m/')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    # def __str__(self):
    #     return 'Praneet'
    