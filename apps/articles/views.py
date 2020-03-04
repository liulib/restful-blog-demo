from articles.models import Category, Articles, Tag
from articles.serializers import CategorySerializers, ArticlesSerializers, TagSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from utils.utils import filter_by_query, get_response
from utils.constants import *


class MyPageNumberPagination(PageNumberPagination):
    """
    分页类
    """
    page_size = 5
    max_page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    分类视图
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(get_response(HANDLE_SUCCESS, serializer.data))


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    标签视图
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializers

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(get_response(HANDLE_SUCCESS, serializer.data))


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    博文视图
    """
    queryset = Articles.objects.filter(is_deleted=False).order_by("-add_time")
    serializer_class = ArticlesSerializers
    pagination_class = MyPageNumberPagination

    def list(self, request, *args, **kwargs):
        params = filter_by_query(request)
        queryset = self.queryset.filter(**params)
        serializer = self.get_serializer(queryset, many=True)
        return Response(get_response(HANDLE_SUCCESS, serializer.data))






