from core.models import Project
from django.db.models import Q


def create_project(user, name, description=''):
    return Project.objects.create(owner=user, name=name, description=description)


def get_project(project_id: int):
    r = Project.objects.filter(id=project_id)
    if len(r) > 0:
        return r[0]


def update_project(project: Project, owner=None, name=None, description=None):
    if owner is not None:
        project.owner = owner
    if name is not None:
        project.name = name
    if description is not None:
        project.description = description
    project.save()
    return project


def delete_project(project):
    pass


def add_user(project, user):
    project.users.add(user)


def remove_user(project, user):
    project.users.remove(user)


def search_project(user, name='', description=''):
    projects = Project.objects.filter(Q(name__contains=name) | Q(description__contains=description))
    return [p for p in projects if p.check_permission(user)]