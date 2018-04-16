from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.paginator import Paginator
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from ProjOther import settings
from app01.models import User, Area


def index(request):
    """进入首页"""

    print('==index==')

    # 出错代码
    # print('aa=' + None)

    return HttpResponse('首页')


def show_static(request):
    """显示静态图片"""
    return render(request, 'show_static.html')


def add_user(request):
    """显示新增用户界面"""
    return render(request, 'add_user.html')


def do_add_user(request):
    """新增用户（上传图片）"""

    # todo: 获取用户上传的图片
    # django.core.files.uploadedfile.InMemoryUploadedFile
    upload_file = request.FILES.get('avatar')
    print(type(upload_file), upload_file.name)

    # 定义头像保存的路径
    filename = upload_file.name  # 文件名
    file_path = settings.MEDIA_ROOT + '/app01/' + filename

    # todo: 保存图片到服务器硬盘中
    with open(file_path, 'wb') as file:
        # 遍历多次，把内容写到文件
        for data in upload_file.chunks():
            file.write(data)

    # 数据库表新增一个用户（保存用户头像路径）
    user = User()
    user.name = request.POST.get('name')
    user.avatar = '/app01/' + filename
    user.save()

    return HttpResponse('新增用户成功')


def show_image(request):
    """显示上传的头像"""

    # 查询所有的用户
    users = User.objects.all()
    # 定义模板显示的字典数据
    context = {'users': users}
    return render(request, 'show_image.html', context)


def show_page(request, page_no):
    """
    分页显示
    :param request:
    :param page_no: 要显示第几页数据
    :return:
    """
    # 查询所有的省份 中国的id为1
    # 方式1
    # area = Area.objects.get(id=1)  # 中国区域对象
    # provinces = Area.objects.filter(parent=area)
    # 方式2
    provinces = Area.objects.filter(parent_id=1)
    # 创建Paginator对象
    # 参数1：要分页的数据
    # 参数２：每页显示多少条数据
    paginator = Paginator(provinces, 10)
    # 获取第一页数据
    page = paginator.page(page_no)

    # 定义字典
    context = {'page': page}
    # 响应请求，返回html界面
    return render(request, 'show_page.html', context)


def show_areas(request):
    """显示区域选择案例"""

    # 获取所有的省份， id=1表示中国
    provinces = Area.objects.filter(parent_id=1)
    # 定义模板数据
    context = {
        'provinces': provinces
    }
    return render(request, 'show_area.html', context)


def get_children(request, pid):
    """
    根据上级区域id，获取下级区域
    :param request:
    :param pid: 上级区域id
    :return:
    """
    # 根据上级区域id，获取下级区域
    areas = Area.objects.filter(parent_id=pid)
    # 定义列表，保存所有的区域数据
    # [[1,'广州'], [2, '深圳']]
    area_list = []
    for a in areas:
        area_list.append([a.id, a.title])

    # 定义字典数据
    context = {
        'areas': area_list
    }

    # { "areas": [
    #   [ 232, "广州市" ],
    #   [ 233, "韶关市" ]
    #  ]
    # }
    return JsonResponse(context)














