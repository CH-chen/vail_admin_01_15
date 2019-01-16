from django.contrib import admin
from goods import models
admin.site.register(models.TypeGoods)
admin.site.register(models.Goods)
admin.site.register(models.Company)
admin.site.register(models.OrderInfo)