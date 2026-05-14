from rest_framework.viewsets import ModelViewSet
from bookstore.pagination import CustomPageNumberPagination
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    pagination_class = CustomPageNumberPagination
