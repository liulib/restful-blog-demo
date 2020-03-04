"""restful_blog_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from restful_blog_demo.settings import MEDIA_ROOT
from django.views.static import serve
from . import settings
from articles.views import CategoryViewSet, ArticleViewSet, TagViewSet
from users.views import CommentsViewSet
from rest_framework.routers import DefaultRouter

import xadmin
# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'article', ArticleViewSet)
router.register(r'tag', TagViewSet)
router.register(r'comments', CommentsViewSet)


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'api/', include(router.urls)),

    # 配置上传文件处理函数
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),

    # ckeditor路径配置
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
  import debug_toolbar
  urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),
  ] + urlpatterns
