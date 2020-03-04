# -*- coding: UTF-8 -*-
__author__ = 'liulib'
__date__ = '2019/3/14 12:02'

import xadmin
from .models import Comments, UserMessage, UserFavorite


class CommentsAdmin(object):
    list_display = ['user', 'article', 'comment', 'add_time']
    search_fields = ['user', 'article', 'comment', 'add_time']
    list_filter = ['user', 'article', 'comment', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'article', 'add_time']
    search_fields = ['user', 'article', 'add_time']
    list_filter = ['user', 'article', 'add_time']


xadmin.site.register(Comments, CommentsAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
