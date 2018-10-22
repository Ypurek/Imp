from django.contrib.auth.models import User
from django.db.models import Q


def get_users_by_list(user_list):
    return User.objects.filter(Q(username__in=user_list) | Q(email__in=user_list))


def get_user_by_email(email):
    us = User.objects.filter(email=email)
    if len(us) == 1:
        return us[0]


def get_user_by_name(name):
    us = User.objects.filter(username=name)
    if len(us) == 1:
        return us[0]


def create_user(username, email, password):
    return User.objects.create(username=username,
                               email=email,
                               password=password)
