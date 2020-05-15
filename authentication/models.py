from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):

    CHOICES = (
        ('H', 'Hospital'),
        ('C', 'Clinic'),
       
    )
    role = models.CharField(max_length=1, choices=CHOICES)

class Hospital(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="hospital_account"
    )


class Clinic(models.Model):
    
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="clinic_account"
    )