from django.conf.urls import url

from goods import views
urlpatterns = [
    url(r'^goods/$', views.goods),
    url(r'^goods/(\d+)/$', views.goods),
    url(r'^goods/search/$', views.search),
    # url(r'^goods/delete/(\d+)/$', views.delete),
    # url(r'^goods/delete_all/$', views.delete_all),
    # url(r'^goods/edit/$', views.edit),
    # url(r'^goods/add/$', views.add),
    # url(r'^goods/check_user/$', views.check_user),
    url(r'^orders/$', views.orders),
    # url(r'^orders/(\d+)/$', views.orders),
    url(r'^orders/detail/$', views.order_detail),
    url(r'^orders/add/$', views.order_add),
    # url(r'^orders/search/$', views.search),

]
