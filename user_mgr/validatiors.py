from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_user_exists(value):
    res = User.objects.filter(username=value)
    if len(res) != 0:
        raise ValidationError('username already registered', params={'value': value})


def validate_email_exists(value):
    res = User.objects.filter(email=value)
    if len(res) != 0:
        raise ValidationError('email already registered', params={'value': value})
