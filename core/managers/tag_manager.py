from core.models import TestTag, RunTag


def create_test_tag(name, description=None):
    result = TestTag.objects.get_or_create(name=name)
    if result[1] and description is not None:
        result[0].description = description
        result[0].save()
    return result[0]


def create_run_tag(name, description=None):
    return RunTag.objects.create(name=name, description=description)


def get_test_tags(name=None, description=None):
    return TestTag.find(name, description)