from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, OrderSchemaViewSet, UserViewSet, CustomizeSchemaViewSet

# Setting up the router
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderSchemaViewSet)
router.register(r'users', UserViewSet)
router.register(r'customize', CustomizeSchemaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API URLs
]
