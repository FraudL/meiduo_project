# from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        """
        主页
        :param request:
        :return:
        """
        # return HttpResponse("我是 主页 ....")
        return render(request, 'index.html')
