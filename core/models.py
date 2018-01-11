from django.db import models
import datetime as dt


class Project(models.Model):
    name = models.CharField(default='',
                            null=False,
                            max_length=100)
    description = models.CharField(default='',
                                   null=False,
                                   blank=True,
                                   max_length=2000)


class Tag(models.Model):
    name = models.CharField(default='',
                            null=False,
                            max_length=100,
                            unique=True)
    description = models.CharField(default=None,
                                   null=True,
                                   max_length=140)


class Status(models.Model):
    status = models.CharField(default='',
                              null=False,
                              max_length=50,
                              unique=True)


class TestCase(models.Model):
    summary = models.CharField(default='',
                               null=False,
                               max_length=100)
    tags = models.ManyToManyField(Tag)
    body = models.CharField(default=None,
                            null=True,
                            max_length=2000)
    version = models.SmallIntegerField(default=1)


class TestRun(models.Model):
    test_case = models.ForeignKey(TestCase,
                                  on_delete=models.CASCADE,
                                  related_name='run')
    status = models.ForeignKey(Status,
                               default=None,
                               null=True,
                               on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(default=dt.datetime.now(),
                                     null=False)
    tags = models.ManyToManyField(Tag)
    comment = models.CharField(default='',
                               max_length=1000)
    version = models.SmallIntegerField(default=1)


# TODO plan to remove. Make test run copy on TR change
class TestRunHistory(models.Model):
    test_run = models.ForeignKey(TestRun,
                                 on_delete=models.CASCADE,
                                 related_name='history')
    timestamp = models.DateTimeField(default=dt.datetime.now(),
                                     null=False)
    status = models.ForeignKey(Status,
                               default=None,
                               null=True,
                               on_delete=models.SET_NULL)
    comment = models.CharField(default=None,
                               null=True,
                               max_length=1000)


class TestCaseHistory(models.Model):
    test_case = models.ForeignKey(TestCase,
                                  on_delete=models.CASCADE,
                                  related_name='history')
    summary = models.CharField(default=None,
                               null=True,
                               max_length=100)
    body = models.CharField(default=None,
                            null=True,
                            max_length=2000)
    version = models.SmallIntegerField(default=1)
