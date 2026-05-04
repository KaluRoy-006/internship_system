from django.db import models
from django.contrib.auth.models import User

class ApplicantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    school = models.CharField(max_length=150, blank=True)
    field_of_study = models.CharField(max_length=150, blank=True)
    level = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - Profile"