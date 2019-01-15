dic = {'1':'试用期', '2':'在职','3':'离职'}
print(list(dic.keys())[list(dic.values()).index("离职")])
print(dic.values())
if '在职' in dic.values():
    print(list(dic.keys())[list(dic.values()).index("在职")])

< tr class ="row1 selected" >
< td class ="action-checkbox" >
< input type="checkbox" name="_selected_action" value="9" class ="action-select" > < / td >
< th class ="field-__str__" > < a href="/admin/rbac/userinfo/9/change/" > bbb < / a > < / th > < / tr >