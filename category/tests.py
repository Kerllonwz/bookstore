from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category


class CategoryViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_category(self):
        response = self.client.post('/api/categories/', {'name': 'Fiction'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_categories(self):
        Category.objects.create(name='Science')
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
