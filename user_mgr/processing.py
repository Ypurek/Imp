from django.contrib.auth.models import User
from django.db.models import Q


def get_users_by_list(user_list):
    return User.objects.filter(Q(username__in=user_list) | Q(email__in=user_list))