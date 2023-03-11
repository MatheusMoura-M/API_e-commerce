from rest_framework.test import APITestCase


class LoginTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/login/"

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_login_without_required_fields(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_login_with_required_fields(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_login_wrong_credentials(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)
