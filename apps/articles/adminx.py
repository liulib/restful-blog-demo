# -*- coding: UTF-8 -*-
__author__ = 'liulib'
__date__ = '2019/3/14 12:02'

import xadmin
from .models import Category, Articles, Tag


class CategoryAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


class TagAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


class ArticlesAdmin(object):
    list_display = ['title', 'content', 'add_time', 'recommend', 'read_nums', 'fav_nums', 'category', 'author']
    search_fields = ['title', 'author']
    list_filter = ['title', 'content', 'add_time', 'recommend', 'read_nums', 'fav_nums', 'category', 'author']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Articles, ArticlesAdmin)
