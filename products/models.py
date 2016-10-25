from django.conf import settings
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, blank=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

#Provisional model
class Client(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class ProductInstance(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, blank=True)
    product = models.ForeignKey(Product, blank=True)
    client = models.ForeignKey(Client, blank=True)

    def __str__(self):
        return self.name


#Provisional model
class Local(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=40, unique=True)
    place_id = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class Provision(models.Model):
    product_instances = models.ManyToManyField(ProductInstance)
    local = models.ForeignKey(Local)

    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()

    # def __str__(self):
    #     return self.name

class ProductStatus(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, blank=True, null=True)

    def __str__(self):
        return self.name

class ProductData(models.Model):
    product_instance = models.ForeignKey(ProductInstance)
    local = models.ForeignKey(Local)
    provision = models.ForeignKey(Provision, blank=True, null=True)

    price = models.FloatField(blank=True, null=True)
    shelf_share = models.IntegerField(blank=True, null=True)
    shelf_stock = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey(ProductStatus, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)
