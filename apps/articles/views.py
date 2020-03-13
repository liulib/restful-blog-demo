from articles.models import Category, Articles, Tag
from articles.serializers import CategorySerializers, ArticlesSerializers, TagSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, InvalidPage


from utils.utils import filter_by_query, get_response
from utils.constants import *


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

    def list(self, request, *args, **kwargs):
        params = filter_by_query(request)
        queryset = self.queryset.filter(**params)
        page = request.GET.get('page')
        size = request.GET.get('size')
        if not page:
            page = 1
        if not size:
            size = 1
        paginat = Paginator(queryset, size)
        paged = paginat.page(page)
        try:  # 判断是否有下一页
            has_next = paged.has_next()
            down_page = paged.next_page_number()  # 获取一下页的页码
        except EmptyPage:  # 如果下一页为空的话，
            down_page = paged.paginator.num_pages  # 获取最后一页的页码
            paged = paginat.page(down_page)
        try:
            has_previous = paged.has_previous()  # 判断是否有上一页
            up_page = paged.previous_page_number()  # 获取上页的页码
        except InvalidPage:  # 如果没有上一页
            up_page = 1  # 返回第一页
            paged = paginat.page(up_page)
        serializer = self.get_serializer(paged, many=True)
        res_data = get_response(HANDLE_SUCCESS, serializer.data)
        # 将分页信息写到一个字典中
        tmp = {}
        tmp["page_list"] = [i for i in paginat.page_range]
        tmp["has_previous"] = has_previous
        tmp["has_next"] = has_next
        tmp["previous_page_number"] = up_page
        tmp["next_page_number"] = down_page
        tmp["page_number"] = paged.number
        res_data["page_links"] = tmp
        return Response(res_data)






