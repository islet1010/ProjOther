from django.contrib import admin

from app01.models import Area, User


class AreaInline(admin.StackedInline):
    model = Area    # 关联子对象（多类对象）


class AreaInline2(admin.TabularInline):
    model = Area    # 关联子对象（多类对象）


class AreaAdmin(admin.ModelAdmin):
    """模型管理类： 控制模型在管理后台的显示样式"""
    # 要在后台显示哪此字段
    list_display = ['id', 'title','parent_area']
    # 每页显示多少条
    list_per_page = 10
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True

    # 搜索区域名称
    search_fields = ['title']
    # 要在编辑界面编辑哪些字段
    # fields = ['parent', 'title']
    # 分组显示 与fields不能同时使用
    fieldsets = (
        ('基本', {'fields': ('title',)}),
        ('高级', {'fields': ('parent',)}),
    )

    # 编辑关联对象（下级区域）
    # inlines = [AreaInline]
    inlines = [AreaInline2]


admin.site.register(Area, AreaAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'avatar']


admin.site.register(User, UserAdmin)

















