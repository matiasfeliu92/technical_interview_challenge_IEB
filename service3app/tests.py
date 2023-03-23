import unittest
from django.urls import reverse
from django.test import TestCase
from .models import Products

class ProductListTest(TestCase):
    def setUp(self):
        self.url_all_products = reverse('get_all_products')
        self.url_one_product = reverse('get_one_product')  # test for get on product by code

    def test_status_code(self):
        # response = self.client.get(self.url_all_products)
        response = self.client.get(self.url_one_product)
        self.assertEqual(response.status_code, 200)