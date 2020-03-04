from operations.models import Comments
from users.serializers import CommentsSerializers
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


class CommentsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    评论视图
    """
    queryset = Comments.objects.order_by("-add_time")
    serializer_class = CommentsSerializers
    pagination_class = MyPageNumberPagination

    def list(self, request, *args, **kwargs):
        if request.GET.get('article'):
            params = filter_by_query(request)
            queryset = self.queryset.filter(**params)
            serializer = self.get_serializer(queryset, many=True)
            return Response(get_response(HANDLE_SUCCESS, serializer.data))
        else:
            return Response(get_response(HANDLE_FAIL, ""))





