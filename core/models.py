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
                            max_length=100)


class Status(models.Model):
    status = models.CharField(default='',
                              null=False,
                              max_length=50)


class TestCase(models.Model):
    name = models.CharField(default='',
                              null=False,
                              max_length=100)
    tags = models.ManyToManyField(Tag)


class TestRun(models.Model):
    test_case = models.ForeignKey(TestCase,
                                  on_delete=models.CASCADE,
                                  related_name='run')
    status = models.ForeignKey(Status,
                               default=None,
                               null=True,
                               on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    comment = models.CharField(default='',
                               max_length=1000)


class TestRunHistory(models.Model):
    test_run = models.ForeignKey(TestRun,
                                 on_delete=models.CASCADE,
                                 related_name='history')
    timestamp = models.DateTimeField(default=dt.datetime.now(),
                                     null=False)
