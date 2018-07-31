from .models import *


def get_project(id=None, name=None):
    if id is not None:
        return Project.objects.get(id=id)
    elif name is not None:
        return Project.objects.filter(name__contains=name)


def add_test_tag(name, description=None):
    tt = TestTag.objects.filter(name=name)
    if len(tt) == 0:
        return TestTag.objects.create(name=name, description=description)
    else:
        return tt[0]


def create_test(project_id, author, title, tags=None, body=None, attachs=None):
    p =
    if p.owner == author or author in p.users.all():
        t = TestCase.objects.create(project=p, author=author, title=title, body=body)
        if tags is not None:
            for tag in tags:
                t.tags.add(add_test_tag(tag))
            t.save()
        if attachs is not None:
            pass
    else:
        raise PermissionError('no permission to create tests for project')
    return t


def update_test(test_id, author, title=None, body=None):
