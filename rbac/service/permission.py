

def init_session(user,request):
    # 查询当前登录用户的所有角色
    ret = user.roles.all().values("permission__url").distinct()  # 去重复
    print(ret)

    permission_list = []
    for item in ret:
        permission_list.append(item["permission__url"])
        print(permission_list)
        # 在session中注册用户权限
    request.session["permission_list"] = permission_list
