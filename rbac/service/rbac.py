
from django.shortcuts import HttpResponse,redirect
from django.utils.deprecation import MiddlewareMixin
import re

class ValidPermission(MiddlewareMixin):

    def process_request(self,request):

        #获取当前路径
        current_path = request.path_info

        #校验白名单
        valid_url_list = ["/login/","/reg/","/admin/.*"]
        for valid_url in valid_url_list:
            ret = re.match(valid_url,current_path)
            if ret:
                return None

        #校验是否登录

        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("/login/")

        #校验权限
        permission_list = request.session["permission_list"]  # "users","users/delete/6"
        print(permission_list)
        print("*******")
        # 获取当前的网址，判断当前网址是否在保存的session值中
        # current_path = request.path_info

        flag = False
        for permission in permission_list:
            permission = "^%s$" % permission
            ret = re.match(permission, current_path)
            if ret:
                flag = True
                break

        if not flag:
            return HttpResponse('没有权限')

        return None