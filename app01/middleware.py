from django.http.response import HttpResponse


class MyMiddleware(object):
    """自定义中间件类"""

    def __init__(self):
        """服务器启动后，处理第一个请求时调用"""
        print('---init--')

    def process_request(self, request):
        """django创建request对象后，url匹配之前调用"""
        print('--process_request--')

        # # 禁止某ip访问网站
        # ip = request.META.get('REMOTE_ADDR')
        # if ip in ['127.0.0.1']:  # 如果是黑名单，则禁止访问
        #     return HttpResponse('禁止访问')

    def process_view(self, request, view_func, view_args, view_kwargs):
        """url匹配后，视图函数执行前调用"""
        print('--process_view--')

    def process_response(self, request, response):
        """视图函数执行后，返回内容给浏览器之前调用"""
        print('--process_response--')
        return response

    def process_exception(self, request, exception):
        """视图函数执行出错时调用"""
        print('--process_exception--')

        # 处理出错，自定义返回的html界面内容
        # return HttpResponse('出错了: %s' % exception)


class MyMiddleware2(object):

    def __init__(self):
        print('---init2--')

    def process_request(self, request):
        print('--process_request2--')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('--process_view2--')

    def process_response(self, request, response):
        print('--process_response2--')
        return response

    def process_exception(self, request, exception):
        print('--process_exception2--')




