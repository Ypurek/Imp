from django.test import TestCase
from core import models as m


class CheckRunModelTest(TestCase):
    def setUp(self):
        project = m.Project(name='test')
        self.tc = m.TestCase(project=project, summary='new test1')

    def test_run_defaults(self):
        run = m.TestRun(test_case=self.tc)
        self.assertIsNone(run.timestamp)
        self.assertEqual(run.status, 'NR')
