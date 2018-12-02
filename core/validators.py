from django.core.exceptions import ValidationError
from .models import Project


def check_if_array(value):
    if type(value) != list:
        raise ValidationError('data expected in list format', params={'value': value})


def check_if_array_contains_str(value):
    for x in value:
        if type(x) != str:
            raise ValidationError('value in array is not string', params={'value': x})


def check_if_project_unique(value):
    if len(Project.objects.filter(name=value)) != 0:
        raise ValidationError('Project name already exist', params={'value': value})