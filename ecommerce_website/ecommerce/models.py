from django.db import models

# Create your models here.

class Order_Product(models.Model):
    order = models.ForeignKey("Order")
    product = models.ForeignKey("Product")
    count = models.IntegerField("Count")
    price = models.IntegerField("Price")

    def __str__(self):
        return str('ID ' + str(self.order.id))


class Product(models.Model):
    name = models.CharField("Name", max_length=30)
    description = models.CharField("Description", max_length=30, blank=True)
    price = models.IntegerField("Price")
    image = models.FileField("Image", upload_to="", blank=True)
    stock = models.IntegerField("Stock")
    is_enabled = models.BooleanField("Enabled", default=True)
    created_at = models.DateTimeField("Created Time", auto_now_add=True)
    updated_at = models.DateTimeField("Updated Time", auto_now=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    postal_code = models.CharField("Zip", max_length=30)
    prefecture = models.CharField("Prefecture", max_length=30)
    city = models.CharField("City", max_length=30)
    street1 = models.CharField("Street Address1", max_length=30)
    street2 = models.CharField("Street Address 2", max_length=30, blank=True)
    tel = models.CharField("Tel", max_length=30, blank=True)
    email = models.CharField("メールアドレス", max_length=200)
    created_at = models.DateTimeField("Created Time", auto_now_add=True)
    updated_at = models.DateTimeField("Updated Time", auto_now=True)

    def __str__(self):
        return self.first_name + self.last_name

class Order(models.Model):
    ordered_at = models.DateTimeField("Ordered Time", auto_now_add=True)
    created_at = models.DateTimeField("Created Time", auto_now_add=True)
    updated_at = models.DateTimeField("Updated Time", auto_now=True)
    customer = models.ForeignKey("Customer")
    payment = models.ForeignKey("Payment")
    products = models.ManyToManyField(Product, through=Order_Product)

    def __str__(self):
        return str('ID ' + str(self.id))


class Payment(models.Model):
    name = models.CharField("Name", max_length=30)
    payment_type = models.CharField("Payment type", max_length=30)

    def __str__(self):
        return self.name
