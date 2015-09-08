from django.test import TestCase
from orm.models import TestCaseModel
from orm.utils import get_by_uuid

class GetByUUIDTestCase(TestCase):

    def setUp(self):
        self.uuid = '6bc4d337-44ca-4984-9a14-17f81aeebdff'

    def test(self):
        self.assertIsNone(get_by_uuid(self.uuid, field_name='uuid'))

    def test_one(self):
        model = TestCaseModel.objects.create(uuid=self.uuid)
        self.assertEqual(get_by_uuid(self.uuid, field_name='uuid'), model)
