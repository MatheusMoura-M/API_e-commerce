from rest_framework.test import APITestCase


class AddressTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/users/"

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_address_create_without_required_fields(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_address_create_with_required_fields(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_address_update(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)
