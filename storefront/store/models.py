# Importing models from django.db so that it can create a database with the fields we provided below
from django.db import models


# Promotion class contains the promotions which can be applied to the product
class Promotion(models.Model):
    # Description of the promotion
    description = models.CharField(max_length=255)
    discount = models.FloatField()  # Discount for the promotion


# Collection class which contains the information about a collection of a user
class Collection(models.Model):
    title = models.CharField(max_length=255)  # Title/Name of the collection
    featured_product = models.ForeignKey(
        # Product added to the collection
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')


# Product class which stores the information about the product
class Product(models.Model):
    title = models.CharField(max_length=225)  # Title/Name of the Product
    slug = models.SlugField()  # Slug of the Product
    description = models.TextField()  # Description/About the Product
    price = models.DecimalField(
        max_digits=6, decimal_places=2)  # Price of the Prodcut
    # Quantity present in the inventory of the Product
    inventory = models.IntegerField()
    # last update history of the Product
    last_update = models.DateTimeField(auto_now=True)
    # Collection containing this product
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    # Promotions which can be applied to the product (ManytoManyField)
    promotions = models.ManyToManyField(Promotion)


# Customer class which stores the information about customer
class Customer(models.Model):

    # Memberships of the customer
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    # Membership choices for the customer
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    first_name = models.CharField(max_length=255)  # First name of the customer
    last_name = models.CharField(max_length=255)  # Last name of the customer
    email = models.EmailField(unique=True)  # Email of the customer
    phone = models.CharField(max_length=255)  # Mobile number of the customer
    birth_date = models.DateField(null=True)  # Date of birth of the customer
    membership = models.CharField(
        # Activer membership of the customer
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


# Order class which contains the information about the order
class Order(models.Model):

    # Status of payment of order
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    # Payment status choice of order
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    # Time when the order was placed
    placed_at = models.DateTimeField(auto_now_add=True)

    payment_status = models.CharField(
        # Payment status of order
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)

    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT)  # Customer assosiated by order


# OrderItem class contains the information about a particular item from an order
class OrderItem(models.Model):
    # Order for which the item is stored
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT)  # Item for the order
    quantity = models.PositiveSmallIntegerField()  # Number of Items
    unit_price = models.DecimalField(
        max_digits=6, decimal_places=2)  # Price of the Item (a Unit)


# Address class contains the geographic information of every user
class Address(models.Model):
    street = models.CharField(max_length=255)  # Street of the user
    city = models.CharField(max_length=255)  # City of the user
    customer = models.OneToOneField(
        # Customer information for the address
        Customer, on_delete=models.CASCADE, primary_key=True)


# Cart class contains the information about the cart
class Cart(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True)  # When the cart was created


# CartItem class contains the information about the items present in the cart
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # Carts
    # Products present in the cart
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Number of item present in the cart
    quantity = models.PositiveSmallIntegerField()
