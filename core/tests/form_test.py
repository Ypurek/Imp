import json
from django.test import TestCase
from core.forms import CreateTestForm


# class CreateTestFormTest(TestCase):
#     def setUp(self):
#         self.post = {'project_id': 1,
#                      'name': 'to do some tests',
#                      'body': 'body'}
#
#     def test_only_mandatory_pos(self):
#         f = CreateTestForm(self.post)
#         self.assertTrue(f.is_valid())
#         self.assertIsNone(f.cleaned_data.get('tags'))
