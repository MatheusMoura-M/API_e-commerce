from rest_framework.test import APITestCase


class ProductTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/products/"

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_users_pagination_with_admin_token(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_users_pagination_no_authentication(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_create_user_without_required_fields(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_create_user_with_required_fields(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_create_user_duplicated_email(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_create_user_duplicated_username(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_users_pagination(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)
