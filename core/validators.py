from django.core.exceptions import ValidationError


def check_if_array(value):
    if type(value) != list:
        raise ValidationError('Features provided not in list format', params={'value': value})


def check_if_array_contains_str(value):
    for x in value:
        if type(x) != str:
            raise ValidationError('feature not in string format', params={'value': x})
