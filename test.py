from app import app
from unittest import TestCase

from forex_python.converter import CurrencyRates, Decimal, RatesNotAvailableError

c = CurrencyRates(force_decimal=True)

class ConvertTestCase(TestCase):

    def setUp(self):
        print("SET UP")

    def tearDown(self):
        print("TEAR DOWN")

    def test_route(self):
        with app.test_client() as client:
            res = client.get('/')
            self.assertEqual(res.status_code, 200)

    def test_convert(self):
        with app.test_client() as client:
            res = client.get('/convert')
            self.assertEqual(c.convert('USD', 'USD', 1), 1)

    # I also want to be able to test the redirect
    # def test_redirect(self):
    #     with app.test_client() as client:
    #         res = client.get('/')
    #         self.assertEqual(res.status_code, 302)
