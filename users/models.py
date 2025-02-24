from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ROLES = {
        "student": "Student",
        "teacher": "Teacher"
    }
    
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=15, choices=[(v, v) for v in ROLES.values()], default="Student")


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
