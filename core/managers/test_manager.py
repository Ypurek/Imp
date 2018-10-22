from core.models import TestCase
from .tag_manager import *


def create_test(project, author, summary, tags=None, body=None):
    test = TestCase(project=project, summary=summary, author=author, body=body)
    if tags is not None:
        for tag in tags:
            test.tags.add(create_test_tag(tag))
    test.save()
    return test


def get_test(id):
    t = TestCase.objects.filter(id=id)
    if len(t) == 1:
        return t[0]