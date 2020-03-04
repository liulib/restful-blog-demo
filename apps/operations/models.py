from django.db import models
from datetime import datetime

from users.models import UserProfile
from articles.models import Articles
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel
# Create your models here.


class Comments(MPTTModel):
    user = models.ForeignKey(UserProfile, verbose_name='评论用户')
    article = models.ForeignKey(Articles, verbose_name='评论博文')
    comment = RichTextField(verbose_name='评论内容', config_name='comments')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')
    parent = models.ForeignKey('self', verbose_name='对应ID', null=True, blank=True, related_name='children')

    class Meta:
        ordering = ['-add_time']
        verbose_name = '博文评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment

    class MPTTMeta:
        order_insertion_by = ['-add_time']


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="接收用户")
    message = models.TextField(verbose_name='消息内容')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='点赞用户')
    article = models.ForeignKey(Articles, verbose_name='点赞博文')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='点赞时间')

    class Meta:
        verbose_name = '用户收藏表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user

