from core.models import Project


def create_project(user, name, description=''):
    return Project.objects.create(owner=user, name=name, description=description)


def get_project(project_id):
    r = Project.objects.filter(id=project_id)
    if len(r) > 0:
        return r[0]


def update_project(project, owner=None, name=None, description=None):
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


