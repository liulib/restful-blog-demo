from django.db import models
from datetime import datetime
from django.urls import reverse
from users.models import UserProfile
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Category(models.Model):
    """
    分类模型
    """
    name = models.CharField(max_length=50, verbose_name='分类名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '博文分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签 模型
    """
    name = models.CharField(max_length=50, verbose_name='分类名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=60, verbose_name='博文标题')
    brief = models.CharField(max_length=500, verbose_name='博文摘要', default='')
    content = RichTextUploadingField(verbose_name='博文内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(default=datetime.now, verbose_name='最后更新时间')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')
    recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    read_nums = models.IntegerField(default=0, verbose_name='阅读数')
    fav_nums = models.IntegerField(default=0, verbose_name='点赞数')
    category = models.ForeignKey(Category, verbose_name='所属分类')
    tag = models.ForeignKey(Tag, verbose_name='标签')
    author = models.ForeignKey(UserProfile, verbose_name='作者')

    def increase_views(self):
        self.read_nums += 1
        self.save(update_fields=['read_nums'])

    def comment_nums(self):
        # 获取评论的数量
        from operations.models import Comments
        return Comments.objects.filter(article=self).count()

    class Meta:
        verbose_name = '博文详细信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.pk})
