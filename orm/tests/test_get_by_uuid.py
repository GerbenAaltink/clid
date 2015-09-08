import uuid
from django.test import TestCase
from orm.models import TestCaseModel
from orm.utils import get_by_uuid

class GetByUUIDTestCase(TestCase):

    def setUp(self):
        self.uuid = uuid.uuid4()

    def test(self):
        self.assertIsNone(get_by_uuid(self.uuid, field_name='uuid'))

    def test_one(self):
        TestCaseModel.objects.create(uuid=self.uuid)
        self.assertEqual(get_by_uuid(self.uuid, field_name='uuid').uuid, self.uuid)
