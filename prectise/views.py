from rest_framework import viewsets
from .models import Category, Product, OrderSchema, User, customizeSchema
from .serializers import CategorySerializer, ProductSerializer, OrderSchemaSerializer, UserSerializer, CustomizeSchemaSerializer

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Order Schema ViewSet
class OrderSchemaViewSet(viewsets.ModelViewSet):
    queryset = OrderSchema.objects.all()
    serializer_class = OrderSchemaSerializer

# Customize Schema ViewSet
class CustomizeSchemaViewSet(viewsets.ModelViewSet):
    queryset = customizeSchema.objects.all()
    serializer_class = CustomizeSchemaSerializer

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
