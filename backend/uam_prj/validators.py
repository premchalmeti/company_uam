from django.core.validators import RegexValidator


mobile_validator = RegexValidator(
    regex=r'^\+\d{1,3}-[0-9]{9,15}$', 
    message='phone number enter must be in format +1[23]-123456789[123456]'
)
