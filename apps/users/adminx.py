# -*- coding: UTF-8 -*-
__author__ = 'liulib'
__date__ = '2019/3/13 16:56'

import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time', 'status']
    search_fields = ['code', 'email', 'send_type', 'status']
    list_filter = ['code', 'email', 'send_type', 'send_time', 'status']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "博客后台管理"
    site_footer = "liulib"
    menu_style = "accordion"


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
