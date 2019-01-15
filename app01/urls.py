from django.conf.urls import url

from app01 import views
urlpatterns = [
    url(r'^user/$', views.users),
    url(r'^user/(\d+)/$', views.users),
    url(r'^user/search/$', views.search),
    url(r'^user/delete/(\d+)/$', views.delete),
    url(r'^user/delete_all/$', views.delete_all),
    url(r'^user/edit/$', views.edit),
    url(r'^user/add/$', views.add),
    url(r'^user/check_user/$', views.check_user),
]
