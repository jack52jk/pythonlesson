from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class CollectHostInfo(View):
 
    #处理get请求 
    def get(self,request):
        pass
    #处理Post请求
    def post(self,request):
        print(request.POST)
        return HttpResponse("sucess-----------------")
