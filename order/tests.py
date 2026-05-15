from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from category.models import Category
from product.models import Product
from .models import Order


class OrderViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        category = Category.objects.create(name='Fiction')
        self.product = Product.objects.create(name='Dune', price='29.90', category=category)
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_order_authenticated(self):
        data = {'product': self.product.id, 'quantity': 2}
        response = self.client.post('/api/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(response.data['quantity'], 2)

    def test_list_orders_authenticated(self):
        Order.objects.create(product=self.product, quantity=1)
        Order.objects.create(product=self.product, quantity=3)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_create_order_unauthenticated(self):
        self.client.credentials()
        data = {'product': self.product.id, 'quantity': 1}
        response = self.client.post('/api/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_orders_unauthenticated(self):
        self.client.credentials()
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
