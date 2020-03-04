from django.db import models

from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=40, verbose_name='用户昵称', default='')
    birthday = models.DateField(verbose_name='用户生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), default='female', max_length=20)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def unread_nums(self):
        # 获取用户未读消息的数量
        from operations.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='邮箱验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=(('register', '注册'), ('forget', '找回密码')), max_length=30, verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发生时间')
    status = models.BooleanField(choices=((1, '已使用'), (0, '未使用')), default=0, verbose_name='是否使用')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name="轮播图", max_length=100)
    url = models.CharField(max_length=200, verbose_name='访问地址', null=True, blank=True)
    index = models.IntegerField(default=100, verbose_name='图片顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '首页轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
