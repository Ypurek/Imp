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


class CheckTestTagModelTest(TestCase):
    def setUp(self):
        tag = m.TestTag(name='some name', description='description')
        t2 = m.TestTag(name='alterM', description='incredible')
        tag.save()
        t2.save()

    def test_tag_search_by_name(self):
        self.assertTrue(len(m.TestTag.find(name='name')) == 1)

    def test_tag_search_by_description(self):
        self.assertTrue(len(m.TestTag.find(description='script')) == 1)

    def test_tag_search_by_both(self):
        self.assertTrue(len(m.TestTag.find(name='ome', description='script')) == 1)

    def test_tag_search_2_1(self):
        self.assertTrue(len(m.TestTag.find(description='i')) == 2)

    def test_tag_search_2_2(self):
        self.assertTrue(len(m.TestTag.find(name='some', description='incredible')) == 2)

    def test_tag_search_none(self):
        self.assertTrue(len(m.TestTag.find(name='123', description='456')) == 0)