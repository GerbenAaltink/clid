from unittest import TestCase
from orm.models import TestCaseModel
from orm.utils import get_models


class GetModelsTestCase(TestCase):

    def setUp(self):
        self.ignore_modules = [None, 'django']

    def test(self):
        self.assertTrue(type(get_models()) == list)

    def test_one(self):
        self.assertTrue(TestCaseModel in get_models(self.ignore_modules))

    def test_use_modules(self):
        self.ignore_modules.append(TestCaseModel.__module__)
        self.assertFalse(TestCaseModel in get_models(self.ignore_modules))