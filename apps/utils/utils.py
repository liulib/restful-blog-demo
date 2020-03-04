from rest_framework.views import exception_handler
from utils.constants import STATUS_CODE


def filter_by_query(request):
    """
    根据查询参数过滤结果集合
    """
    params = {}
    # query params
    tag = request.GET.get('tag')
    category = request.GET.get('category')
    article = request.GET.get('article')

    if category:
        params['category'] = category
    if tag:
        params['tag'] = tag
    if article:
        params['article'] = article
    return params


# 错误处理
def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {}
        errors = []
        for field, value in response.data.items():
            errors.append("{} : {}".format(field, " ".join(value)))

        response.data['code'] = None
        response.data['result'] = None
        response.data['message'] = str(exc)
    return response


def get_response(code, res, message=None):
    return {
        'code': code,
        'message': message or STATUS_CODE[code],
        'result': res
    }


