from rest_framework.viewsets import ModelViewSet
from bookstore.pagination import CustomPageNumberPagination
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
