from django import forms
from .settings import *
from .validators import *


class ArrayField(forms.Field):
    def __init__(self, required=False, initial=[], help_text='', label=''):
        self.default_validators = [check_if_array, check_if_array_contains_str]
        super().__init__(required=required, initial=initial, help_text=help_text, label=label)

    def clean(self, value):
        return super().clean(value)


class CreateTestForm(forms.Form):
    project_id = forms.IntegerField(required=True, min_value=1)
    name = forms.CharField(required=True, min_length=TC_NAME_MIN_LEN, max_length=TC_NAME_MAX_LEN)
    body = forms.CharField(required=True, max_length=DESCRIPTION_LENGTH)
    # tags = ArrayField(required=False)


class CreateProjectForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(required=False)

