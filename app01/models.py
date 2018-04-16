from django.db import models


class Area(models.Model):
    """地区类"""
    title = models.CharField(max_length=50,
                             verbose_name='区域名称')
    # 外键： 自关联
    parent = models.ForeignKey('self', null=True, blank=True)

    def parent_area(self):
        """获取上级区域"""

        if self.parent is None:
            # 如果没有上级区域，返回空字符串
            return ''

        return self.parent.title

    # 指定列的名称
    parent_area.short_description = '上级区域'
    # 排序条件
    parent_area.admin_order_field = 'id'

    def __str__(self):
        return self.title


class User(models.Model):
    """用户模型类： 演示图片上传"""

    name = models.CharField(max_length=20)
    # 头像, 上传的图片保存到media/app01目录下
    avatar = models.ImageField(upload_to='app01')






