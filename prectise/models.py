from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Category(models.Model):
    c_name = models.CharField(max_length=255, null=False, blank=False)  # equivalent to String type with `required: true`
    c_description = models.TextField(null=False, blank=False)  # equivalent to String type with `required: true`
    c_image = models.URLField(max_length=200, null=True, blank=True)  # equivalent to String type
    c_status = models.CharField(max_length=255, null=False, blank=False)  # equivalent to String type with `required: true`
    created_at = models.DateTimeField(auto_now_add=True)  # equivalent to `timestamps: true` (creation time)
    updated_at = models.DateTimeField(auto_now=True)  # equivalent to `timestamps: true` (update time)

    class Meta:
        db_table = "categories"  # specifies the database table name

    def __str__(self):
        return self.c_name
    

class customizeSchema(models.Model):
    slider_images = models.CharField(max_length=500,null=False,blank=False)
    firstShow = models.IntegerField(default=0)

    class Meta:
        db_table = "customizeSchema"

    def __str__(self):  # Fix the typo here
        return self.slider_images


class OrderSchema(models.Model):  
    class OrderStatus(models.TextChoices):
        NOT_PROCESSED = "Not processed", "Not Processed"
        PROCESSING = "Processing", "Processing"
        SHIPPED = "Shipped", "Shipped"
        DELIVERED = "Delivered", "Delivered"
        CANCELLED = "Cancelled", "Cancelled"

    all_product = models.JSONField()  # A list of dictionaries containing `id` and `quantity`
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # Reference to the User model
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    transaction_id = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)  # Storing phone as a string is more flexible
    status = models.CharField(
        max_length=15,
        choices=OrderStatus.choices,
        default=OrderStatus.NOT_PROCESSED,
    )
    created_at = models.DateTimeField(auto_now_add=True)  # `timestamps: true` for creation time
    updated_at = models.DateTimeField(auto_now=True)  # `timestamps: true` for update time

    class Meta:
        db_table = "orders"

    def __str__(self):
        return f"Order {self.id} - {self.status}"
    
    class orderstuts(models.TextChoices):
        NOT_PROCESSED = "Not processed", "Not Processed"
        PROCESSING = "Processing", "Processing"
        SHIPPED = "Shipped", "Shipped"
        DELIVERED = "Delivered", "Delivered"
        CANCELLED = "Cancelled", "Cancelled"

    all_product = models.JSONField()  # A list of dictionaries containing `id` and `quantity`
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # Reference to the User model
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    transaction_id = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)  # Storing phone as a string is more flexible
    status = models.CharField(
        max_length=15,
        choices=orderstuts.choices,
        default=orderstuts.NOT_PROCESSED,
    )
    created_at = models.DateTimeField(auto_now_add=True)  # `timestamps: true` for creation time
    updated_at = models.DateTimeField(auto_now=True)  # `timestamps: true` for update time

    class Meta:
        db_table = "orders"

    def __str__(self):
        return f"Order {self.id} - {self.status}"


class Product(models.Model):
    p_name = models.CharField(max_length=255, null=False, blank=False)  # Product name
    p_description = models.TextField(null=False, blank=False)  # Product description
    p_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)  # Product price
    p_sold = models.PositiveIntegerField(default=0)  # Products sold
    p_quantity = models.PositiveIntegerField(default=0)  # Available quantity
    p_category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)  # Foreign key to Category
    p_images = models.JSONField(null=False, blank=False)  # List of image URLs
    p_offer = models.CharField(max_length=255, null=True, blank=True)  # Product offer (nullable)
    p_ratings_reviews = models.JSONField(default=list)  # List of reviews and ratings
    p_status = models.CharField(max_length=50, null=False, blank=False)  # Product status
    created_at = models.DateTimeField(auto_now_add=True)  # Creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Update timestamp

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.p_name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    name = models.CharField(max_length=32, null=False, blank=False)  # User's name
    email = models.EmailField(unique=True, null=False, blank=False)  # Email with uniqueness constraint
    password = models.CharField(max_length=128, null=False, blank=False)  # Hashed password
    user_role = models.PositiveSmallIntegerField(default=0)  # User role (e.g., admin, user)
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # Phone number
    verified = models.BooleanField(default=False)  # Email/Phone verification status
    history = models.JSONField(default=list, blank=True)  # Stores order or activity history
    is_active = models.BooleanField(default=True)  # Account active status
    is_staff = models.BooleanField(default=False)  # Staff user status
    is_superuser = models.BooleanField(default=False)  # Superuser status
    created_at = models.DateTimeField(auto_now_add=True)  # Creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Update timestamp

    # Set email as the username field
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email