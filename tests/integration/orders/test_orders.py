from rest_framework.test import APITestCase


class OrderTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/orders/"

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_order_create_client(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_order_subtraction_on_product(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_order_create_for_different_sellers(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_order_create_with_product_out_stock(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_order_update_seller(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_order_update_non_seller(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)

    def test_order_products_without_stock(self):
        expected = ""
        result = ""
        msg = ""
        self.assertEqual(expected, result, msg)
