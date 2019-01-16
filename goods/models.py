from django.db import models
from rbac.models import *

# Create your models here.
class TypeGoods(models.Model):
    title = models.CharField(max_length=64)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Goods(models.Model):
    title = models.CharField(max_length=64)

    jianjie = models.CharField(max_length=300)
    bid_price = models.DecimalField(max_digits=8,decimal_places=2,default=0,verbose_name="进价")
    bid_num = models.IntegerField(verbose_name="进货数量")
    goods_data = models.DateTimeField(default = timezone.now,verbose_name="日期")
    bid_money = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="进货总价")
    sale_price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="售价")
    sale_num = models.IntegerField(verbose_name="销售数量")
    sale_money = models.DecimalField(max_digits=8, decimal_places=2,verbose_name="销售总价")
    kuncui = models.IntegerField()
    unit = models.CharField(max_length=20,verbose_name="单位")
    actual_paymen = models.DecimalField(max_digits=9, decimal_places=2,verbose_name="实付款",default=0)
    goods_expense = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="运费",default=0)
    profit = models.DecimalField(max_digits=9, decimal_places=2,verbose_name="利润",default=0)
    typegoods = models.ForeignKey(to="TypeGoods")
    def __str__(self):
        return self.title

class Company(models.Model):
    name = models.CharField(max_length=64)
    contact = models.CharField(max_length=32)
    company_address = models.CharField(max_length=128)
    receive_address = models.CharField(max_length=128)
    receiver = models.CharField(max_length=32)
    contact_phone = models.CharField(max_length=128)
    receiver_phone = models.CharField(max_length=128)
    def __str__(self):
        return self.name


class OrderInfo(models.Model):
    order_num = models.CharField(max_length=32)
    order_date = models.DateTimeField()
    order_state = models.CharField(max_length=128)
    order_money = models.DecimalField(max_digits=9,decimal_places=2,verbose_name="订单金额")
    actual_paymen = models.DecimalField(max_digits=9,decimal_places=2,verbose_name="实付款",default=0)
    order_expense = models.DecimalField(max_digits=6,decimal_places=2,verbose_name="运费",default=0)
    order_orther = models.DecimalField(max_digits=7,decimal_places=2,verbose_name="其他支出",default=0)
    profit = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="利润",default=0)
    userinfo = models.ForeignKey(UserInfo)
    company = models.ForeignKey(Company)
    goods = models.ManyToManyField(Goods)
    def __str__(self):
        return self.order_num + "  >>>  "+self.company.name
    




