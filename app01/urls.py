from django.conf.urls import url, include

from app01 import views

urlpatterns = [

    # http://127.0.0.1:8000/index
    url(r'^index$', views.index),
    # http://127.0.0.1:8000/show_static
    url(r'^show_static$', views.show_static),
    # http://127.0.0.1.:8000/add_user
    url(r'^add_user$', views.add_user),
    # http://127.0.0.1.:8000/do_add_user            # 显示新增有界面
    url(r'^do_add_user$', views.do_add_user),       # 新增一个用户
    # http://127.0.0.1.:8000/show_image
    url(r'^show_image$', views.show_image),         # 显示上传的头像
    # http://127.0.0.1:8000/show_page/1
    url(r'^show_page/(\d+)$', views.show_page),         # 显示分页

    # http://127.0.0.1:8000/show_areas
    url(r'^show_areas$', views.show_areas),         # 进入区域选择界面
    # http://127.0.0.1:8000/get_children/上级区域id
    url(r'^get_children/(\d+)$', views.get_children),         # 进入区域选择界面

]