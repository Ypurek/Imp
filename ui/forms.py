from django import forms
from user_mgr.processing import get_users_by_list
from . import validators as v

DESCRIPTION_LENGTH = 2000
USERS_DELIMITER = ','


class ProjectForm(forms.Form):
    name = forms.CharField(required=True,
                           max_length=100,
                           min_length=3,
                           validators=[v.is_project_name_unique])
    description = forms.CharField(required=False,
                                   max_length=DESCRIPTION_LENGTH)
    users = forms.CharField(required=False)

    def get_users(self):
        if self.is_valid() and len(self.cleaned_data['users']) > 0:
            raw_users = self.cleaned_data['users'].split(USERS_DELIMITER)
            raw_users_rdy = tuple(map(str.strip, raw_users))
            return get_users_by_list(raw_users_rdy)


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,
                               min_length=8)