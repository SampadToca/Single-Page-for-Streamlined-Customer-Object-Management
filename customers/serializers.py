from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'phone_number']

    def validate_phone_number(self, value):
        # Add custom validation for the phone number, if needed
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        return value
