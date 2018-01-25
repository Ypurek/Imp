from django.forms import ValidationError
from core.models import Project


def is_project_name_unique(value):
    r = Project.objects.filter(name=value)
    if len(r) > 0:
        raise ValidationError('project name already in use', params={'value': value})
