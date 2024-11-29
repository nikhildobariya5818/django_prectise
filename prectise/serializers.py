from rest_framework import serializers
from .models import Category, Product, OrderSchema, User, customizeSchema

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    p_category = CategorySerializer(read_only=True)  # Nested category representation

    class Meta:
        model = Product
        fields = '__all__'

# Order Schema Serializer
class OrderSchemaSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Displaying the user email (can be adjusted)
    all_product = serializers.JSONField()

    class Meta:
        model = OrderSchema
        fields = '__all__'

# Customize Schema Serializer
class CustomizeSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = customizeSchema
        fields = '__all__'

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    # Nested representation for order history
    history = OrderSchemaSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone_number', 'password','user_role', 'verified', 'history', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at')
