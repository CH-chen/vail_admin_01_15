from django.db import models

# Create your models here.
class TypeGoods(models.Model):
    title = models.CharField(max_length=64)
    isDelete = models.BooleanField(default=False)

class Goods(models.Model):
    title = models.CharField(max_length=64)
    jianjie = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    kuncui = models.IntegerField()
    unit = models.CharField(max_length=20)
    typegoods = models.ForeignKey(to="TypeGoods")

class OrderInfo(models.Model):
    order_num = models.CharField(max_length=32)
    order_date = models.DateTimeField()
    




