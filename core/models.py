from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from .settings import *
import datetime as dt


class Project(models.Model):
    name = models.CharField(default='',
                            null=False,
                            max_length=100,
                            unique=True)
    description = models.CharField(default='',
                                   null=False,
                                   blank=True,
                                   max_length=DESCRIPTION_LENGTH)
    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              related_name='owned_projects',
                              null=True)
    users = models.ManyToManyField(User,
                                   related_name='visible_projects',
                                   default=None)


class TestTag(models.Model):
    name = models.CharField(default='',
                            null=False,
                            max_length=100,
                            unique=True)
    description = models.CharField(default=None,
                                   null=True,
                                   max_length=140)

    @classmethod
    def find(cls, name=None, description=None):
        if name is None and description is None:
            return []
        elif name is not None and description is None:
            return cls.objects.filter(name__contains=name)
        elif name is None and description is not None:
            return cls.objects.filter(description__contains=description)
        else:
            return cls.objects.filter(Q(name__contains=name) | Q(description__contains=description))


class RunTag(models.Model):
    name = models.CharField(default='',
                            null=False,
                            max_length=100,
                            unique=True)
    description = models.CharField(default=None,
                                   null=True,
                                   max_length=140)


class TestCase(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='tests')
    summary = models.CharField(default='',
                               null=False,
                               max_length=100)
    tags = models.ManyToManyField(TestTag)
    body = models.CharField(default=None,
                            null=True,
                            max_length=DESCRIPTION_LENGTH)
    version = models.SmallIntegerField(default=1)
    author = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               related_name='tests',
                               null=True)

    @property
    def status(self):
        run = self.runs.filter(timestamp__isnull=False).latest('id')
        if run is None:
            return 'NR'
        else:
            return run.status


class TestRun(models.Model):
    test_case = models.ForeignKey(TestCase,
                                  on_delete=models.CASCADE,
                                  related_name='runs')
    status = models.CharField(choices=tuple(STATUSES.items()),
                              default='NR',
                              max_length=2,
                              null=False)
    timestamp = models.DateTimeField(default=None,
                                     null=True)
    tags = models.ManyToManyField(RunTag)
    comment = models.CharField(default='',
                               max_length=DESCRIPTION_LENGTH)
    version = models.SmallIntegerField(default=1)
    executor = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 related_name='runs',
                                 null=True)

    def execute(self, status, executor, comment=''):
        self.status = status
        self.timestamp = dt.datetime.now()
        self.executor = executor
        self.comment = comment
        self.version = self.test_case.version
        self.save()


class TestCaseHistory(models.Model):
    test_case = models.ForeignKey(TestCase,
                                  on_delete=models.CASCADE,
                                  related_name='history')
    summary = models.CharField(default=None,
                               null=True,
                               max_length=100)
    body = models.CharField(default=None,
                            null=True,
                            max_length=DESCRIPTION_LENGTH)
    version = models.SmallIntegerField(default=1)
