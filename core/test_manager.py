from .models import *


def create_project(name, description=''):
    return Project.objects.create(name=name, description=description)


