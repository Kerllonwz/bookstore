from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category


class CategoryViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='categoryuser', password='testpass123')

    def test_create_category(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/categories/', {'name': 'Fiction'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_categories(self):
        Category.objects.create(name='Science')
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
