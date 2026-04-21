from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category


class CategoryViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = '/api/categories/'

    def test_create_category(self):
        response = self.client.post(self.list_url, {'name': 'Fiction'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(response.data['name'], 'Fiction')

    def test_list_categories(self):
        Category.objects.create(name='Science')
        Category.objects.create(name='History')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
