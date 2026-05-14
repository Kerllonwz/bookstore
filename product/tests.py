from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from category.models import Category
from .models import Product


class ProductViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='Fiction')
        self.user = User.objects.create_user(username='productuser', password='testpass123')

    def test_create_product(self):
        self.client.force_authenticate(user=self.user)
        data = {'name': 'Dune', 'price': '29.90', 'category': self.category.id}
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_products(self):
        Product.objects.create(name='Dune', price='29.90', category=self.category)
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
