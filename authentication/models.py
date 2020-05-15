from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    '''
    creating a manager for a custom user model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
    '''
    def create_user(self, email,username, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.username=username
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self.db)
        return user

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