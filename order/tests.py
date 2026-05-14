from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from category.models import Category
from product.models import Product
from .models import Order


class OrderViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = '/api/orders/'
        category = Category.objects.create(name='Fiction')
        self.product = Product.objects.create(name='Dune', price='29.90', category=category)

    def test_create_order(self):
        data = {'product': self.product.id, 'quantity': 3}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(response.data['quantity'], 3)

    def test_list_orders(self):
        Order.objects.create(product=self.product, quantity=1)
        Order.objects.create(product=self.product, quantity=2)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 2)
