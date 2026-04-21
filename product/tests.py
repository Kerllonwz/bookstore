from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from category.models import Category
from .models import Product


class ProductViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = '/api/products/'
        self.category = Category.objects.create(name='Fiction')

    def test_create_product(self):
        data = {'name': 'Dune', 'price': '29.90', 'category': self.category.id}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(response.data['name'], 'Dune')

    def test_list_products(self):
        Product.objects.create(name='Dune', price='29.90', category=self.category)
        Product.objects.create(name='Foundation', price='24.90', category=self.category)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
