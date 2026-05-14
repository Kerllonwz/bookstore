from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category


class CategoryViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = '/api/categories/'
        self.user = User.objects.create_user(username='tester', password='password123')

    def test_create_category(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.list_url, {'name': 'Fiction'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(response.data['name'], 'Fiction')

    def test_create_category_requires_authentication(self):
        response = self.client.post(self.list_url, {'name': 'Fiction'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_categories(self):
        Category.objects.create(name='Science')
        Category.objects.create(name='History')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 2)
