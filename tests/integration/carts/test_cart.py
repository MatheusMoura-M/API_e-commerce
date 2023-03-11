from rest_framework.test import APITestCase


class CartTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/carts/"

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_cart_update_with_token(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_cart_update_without_required_fields(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_cart_update_without_product_not_found(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_cart_update_with_one_product(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_cart_update_with_many_products(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)
