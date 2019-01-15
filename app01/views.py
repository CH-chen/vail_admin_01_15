
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from rbac import models
from app01.utils.page import Pagination
from django.db.models import Q
import json

def index(request):

    return render(request, "x-admin/index2.html")

def users(request,num=3):
    current_page = request.GET.get("page",1)
    all_count = models.UserInfo.objects.all().count()
    base_url = request.path
    pagination = Pagination(all_count,int(current_page),base_url,request.GET,per_page=int(num),max_show=6)
    user_list = models.UserInfo.objects.all()[pagination.start:pagination.end]
    import copy
    params = copy.deepcopy(request.GET)
    return render(request, "x-admin/member-list.html",locals())

def search(request):
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)
        dic1 = {'1':'试用期','2':'在职','3':'离职'}
        dic2 = {'1':'男','2':'女'}
        if title:
            if title in dic1.values():
                print(list(dic1.keys())[list(dic1.values()).index(title)])
                # print(list(dic.keys())[list(dic.values()).index("离职")])   #通过字典的值找键
                user_list = models.UserInfo.objects.filter(state=int(list(dic1.keys())[list(dic1.values()).index(title)]))
                return render(request, "x-admin/member-list.html", locals())

            elif title in dic2.values():
                user_list = models.UserInfo.objects.filter(gender=int(list(dic2.keys())[list(dic2.values()).index(title)]))
                return render(request, "x-admin/member-list.html", locals())
            else:
                user_list = models.UserInfo.objects.filter(
                    Q(name__icontains=title) | Q(address__icontains=title) | Q(phone__icontains=title) | Q(
                        entry_time__icontains=title))
                return render(request, "x-admin/member-list.html", locals())

        else:
            return redirect('/user/')
    return render(request, "x-admin/member-list.html", locals())



def add(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        card_id = request.POST.get('card_id')
        address = request.POST.get('address')
        entry_time = request.POST.get('entry_time')
        state = request.POST.get('state')
        roles = request.POST.getlist('roles')
        gender = request.POST.get('gender')
        print(username,password,repassword,phone,email,card_id,address,entry_time,state,roles,gender)
        user = models.UserInfo.objects.create(
            name=username,password=password,phone=phone,
            email=email,card_id=card_id,address=address,
            entry_time=entry_time,state=state,gender=gender
            )#entry_time=entry_time,state=state,gender=gender
        user.roles.set(roles)
        return redirect("/user/")

    user_list = models.UserInfo.objects.all()
    gender_choices = models.UserInfo.gender_choices
    state_choices = models.UserInfo.state_choice
    role_list = models.Role.objects.all()

    return render(request, "x-admin/add-member.html",locals())

def check_user(request):

    username = request.GET.get("username")
    print(username)
    count = models.UserInfo.objects.filter(name=username).count()
    list={"count":count}
    return JsonResponse(list)

def edit(request):
    if request.method == "POST":
        id = request.POST.get("user_id")

        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        card_id = request.POST.get('card_id')
        address = request.POST.get('address')
        entry_time = request.POST.get('entry_time')
        state = request.POST.get('state')
        roles = request.POST.getlist('roles')
        gender = request.POST.get('gender')
        print(id, password, repassword, phone, email, card_id, address, entry_time, state, roles, gender)
        user = models.UserInfo.objects.filter(pk=id).first()
        print(user)


        user.password = password
        user.phone = phone
        user.email = email
        user.card_id = card_id
        user.address = address
        user.entry_time = entry_time
        user.state = state
        user.gender = gender
        user.roles.set(roles)
        user.save()
        print("+++++++++")
        print(id)
        return redirect("/user/")

    id = request.GET.get("id")
    print("999999999")
    print(id)
    user = models.UserInfo.objects.filter(pk=id).first()
    gender_choices = models.UserInfo.gender_choices
    state_choices = models.UserInfo.state_choice
    role_list = models.Role.objects.all()
    print(user.roles.all())
    # for  role in user.roles.all():
    #     print(role)
    # for role in roles_list:
    #     print(role)


    return render(request,"x-admin/edit-member.html",locals())

def delete(request,pk):

    models.UserInfo.objects.filter(id=pk).delete()
    return redirect('/user/')

def delete_all(request):
    #前端发送的ajax请求，后端要返回给前端json字符串
    #如果去掉url后当前有值，则执行删除并跳转，如果去掉url后无值，则返回当前页面12QAAZQ
    user_id = request.GET.get('user_id')
    print(user_id)
    user_id = json.loads(user_id)
    current_url = user_id[0]
    print(user_id)
    user_id.pop(0)  #去掉第一个网址
    print(user_id)
    ret={}
    print(len(user_id))
    if len(user_id):
        models.UserInfo.objects.filter(id__in=user_id).delete()
        print("-----")
        ret = {"url":current_url}
    else:
        print(current_url)
        ret = {'url':current_url}
    return JsonResponse(ret)



def xxxx(request,num=9):
    pass

from rbac.service.permission import *

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.UserInfo.objects.filter(name=username,password=password).first()
        if user:
            ########在session中注册用户id，用于下次登录不用输入用户名密码
            request.session["user_id"] = user.pk
            # ret = user.roles.all()
            # print(ret)

            init_session(user,request)

            return redirect("/index/")
    return render(request,"x-admin/login.html")


