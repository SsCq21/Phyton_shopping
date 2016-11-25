from django.db import models

# Create your models here.

class Order_Product(models.Model):
    order = models.ForeignKey("Order")
    product = models.ForeignKey("Product")
    count = models.IntegerField("注文個数")
    price = models.IntegerField("注文時の価格")

    def __str__(self):
        return str('注文番号 ' + str(self.order.id))


class Product(models.Model):
    name = models.CharField("商品名", max_length=30)
    description = models.CharField("商品説明", max_length=30, blank=True)
    price = models.IntegerField("価格")
    image = models.FileField("商品画像", upload_to="", blank=True)
    stock = models.IntegerField("在庫数")
    is_enabled = models.BooleanField("商品の販売状態", default=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField("名", max_length=30)
    last_name = models.CharField("姓", max_length=30)
    postal_code = models.CharField("郵便番号", max_length=30)
    prefecture = models.CharField("都道府県", max_length=30)
    city = models.CharField("市区町村", max_length=30)
    street1 = models.CharField("番地など", max_length=30)
    street2 = models.CharField("建物名など", max_length=30, blank=True)
    tel = models.CharField("電話番号", max_length=30, blank=True)
    email = models.CharField("メールアドレス", max_length=200)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return self.first_name + self.last_name

class Order(models.Model):
    ordered_at = models.DateTimeField("注文日時", auto_now_add=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)
    customer = models.ForeignKey("Customer")
    payment = models.ForeignKey("Payment")
    products = models.ManyToManyField(Product, through=Order_Product)

    def __str__(self):
        return str('注文番号 ' + str(self.id))


class Payment(models.Model):
    name = models.CharField("決済名", max_length=30)
    payment_type = models.CharField("決済種別", max_length=30)

    def __str__(self):
        return self.name
