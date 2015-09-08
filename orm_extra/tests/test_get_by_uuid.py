from unittest import TestCase
from orm_extra.utils import get_by_uuid


class GetByUUIDTestCase(TestCase):

    def setUp(self):
        self.uuid = '6bc4d337-44ca-4984-9a14-17f81aeebdff'

    def test(self):
        self.assertIsNone(get_by_uuid(self.uuid))
