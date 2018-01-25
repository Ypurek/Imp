from django.db import models
from django.contrib.auth.models import User
import datetime as dt

DESCRIPTION_LENGTH = 2000


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


class Tag(models.Model):
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
    tags = models.ManyToManyField(Tag)
    body = models.CharField(default=None,
                            null=True,
                            max_length=DESCRIPTION_LENGTH)
    version = models.SmallIntegerField(default=1)
    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              related_name='tests',
                              null=True)


class TestRun(models.Model):
    test_case = models.ForeignKey(TestCase,
                                  on_delete=models.CASCADE,
                                  related_name='runs')
    status = models.CharField(choices=(('NR', 'No Run'),
                                       ('PS', 'Passed'),
                                       ('FL', 'Failed'),
                                       ('BL', 'Blocked'),
                                       ('NA', 'Not Available')),
                              default='NR',
                              max_length=2,
                              null=False)
    timestamp = models.DateTimeField(default=dt.datetime.now(),
                                     null=False)
    tags = models.ManyToManyField(Tag)
    comment = models.CharField(default='',
                               max_length=DESCRIPTION_LENGTH)
    version = models.SmallIntegerField(default=1)
    executor = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 related_name='runs',
                                 null=True)


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
