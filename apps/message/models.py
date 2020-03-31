from django.db import models


# Create your models here.
class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, primary_key=True, default="", verbose_name='主键')
    name = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name='用户名')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=100, verbose_name='地址')
    message = models.CharField(max_length=500, verbose_name='留言信息')

    class Meta:
        verbose_name = '用户留言信息'
        verbose_name_plural = verbose_name
        # 设置表名称
        # db_table = 'user_message'
        # 设置默认排序
        # ordering = '-object_id'
