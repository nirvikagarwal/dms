from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer


class CustomRegistrationSerializer(RegisterSerializer):
    CHOICES = (
        ('H', 'Hospital'),
        ('C', 'Clinic'),
       
    )

    role = serializers.ChoiceField(max_length=1, choices=CHOICES)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['role'] = self.validated_data.get('role', '')
        return data_dict