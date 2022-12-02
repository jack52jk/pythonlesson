from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View

from .models import Assets
# Create your views here.

class CmdbView(View):
    def get(self,request):
        obj = Assets.objects.all()

        return render(request,'asset.html',context={'context':obj})


def CmdbDeleteView(request,*args,**kwargs):
    print(request)
    print("args {}".format(args))
    print("kwargs {}".format(kwargs))
    #Assets.objects.get(id=kwargs['pk']).delete()
   # return HttpResponse("OK")
   # return redirect(reverse("cmdb_list"))  == redirect("/api/v1/cmdb")
    return redirect("/api/v1/cmdb")

class CollectHostInfo(View):
 
    #处理get请求 
    def get(self,request):
        pass
    #处理Post请求
    def post(self,request):
        data = request.POST.dict()
        print("*****************************")
        import random
        data['hostname'] +=str( random.randint(1,100))
        data['mac_address'] +=str( random.randint(1,100))
        print("views data is {}".format(data))
        # print(data)
        Assets.objects.create(**data)
        return HttpResponse("sucess-----------------")

def AssetViews(request,*args,**kwargs):
    print(request)
    print("args:{}".format(args))
    print("kwargs: {}".format(kwargs))
    return HttpResponse("sucess")
