from django.shortcuts import render,redirect
from django.http import JsonResponse
from goods import models
from app01.utils.page import Pagination
from django.db.models import Q
import json


def goods(request,num=3):
    goods_list = models.Goods.objects.all()
    current_page = request.GET.get("page", 1)
    all_count = models.Goods.objects.all().count()
    base_url = request.path
    pagination = Pagination(all_count, int(current_page), base_url, request.GET, per_page=int(num), max_show=6)
    goods_list = models.Goods.objects.all()[pagination.start:pagination.end]
    import copy
    params = copy.deepcopy(request.GET)
    return render(request, "x-admin/goods-list.html", locals())

def search(request):
    if request.method == "POST":
        title = request.POST.get('title')

        goods_list = models.Goods.objects.filter(
            Q(title__icontains=title) | Q(typegoods__title__contains=title) | Q(sale_money__icontains=title) | Q(
                goods_data__icontains=title) | Q(orderinfo__company__name__contains=title))

        return render(request, "x-admin/goods-list.html", locals())

    else:
        return redirect('/goods/')
    return render(request, "x-admin/goods-list.html", locals())


def orders(request,num=3):
    order_list = models.OrderInfo.objects.all()
    current_page = request.GET.get("page", 1)
    all_count = models.OrderInfo.objects.all().count()
    base_url = request.path
    pagination = Pagination(all_count, int(current_page), base_url, request.GET, per_page=int(num), max_show=6)
    order_list = models.OrderInfo.objects.all()[pagination.start:pagination.end]
    import copy
    params = copy.deepcopy(request.GET)
    return render(request, "x-admin/order-list.html", locals())

def order_detail(request):
    id = request.GET.get("id")
    print(id)
    order_obj = models.OrderInfo.objects.filter(pk=id).first()

    return render(request, "x-admin/order-detail.html", locals())

def order_add(request):

    return render(request, "x-admin/order-detail.html", locals())



