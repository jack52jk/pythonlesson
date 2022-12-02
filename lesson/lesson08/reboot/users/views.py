from django.shortcuts import render
from django.views import View 
from django.http import HttpRequest,QueryDict,HttpResponse,HttpResponseRedirect
from .models import UserProfile
from django.contrib.auth import authenticate  ,login,logout
from django.urls import reverse
# Create your views here.



 
# def loginView(request:HttpRequest,**kwargs):
#         data=''
     
#         if request.method == 'POST':
#             print(QueryDict(request.body).dict())
        
#             username=QueryDict(request.body).dict().get('username')
#             password=QueryDict(request.body).dict().get('password')
#             users = UserProfile.objects.filter(username = username)
#             print("users is {}".format(type(users)))
#             if username == 'admin' and password == 'admin':
#                 data = 'login sucess'
#                 #return HttpResponseRedirect('/hello/hello/')
                
#             else:
#                 data= 'your username or password error! Please again'
#         dt = {'data':data}
#         return render(request,'hello/login.html',context=dt)

class IndexView(View):
    def get(self,requeset:HttpRequest):
        return render(requeset,'index.html')

 

class LoginView(View):
    def get(self,request:HttpRequest):
        return render(request,template_name='login.html')

    def post(self,request:HttpRequest):
        username = QueryDict( request.body).dict().get('username')
        password = QueryDict(request.body).dict().get('password')
        print('username is {},password is {}'.format(username,password))
        #users = UserProfile.objects.filter(username = username)
        users = authenticate(username=username,password=password)
        print ("users is {},{}".format(users,type(users)))
        if users:
           if users.is_active:
            login(request,users)  #生成登录成功后访问任何页面的认证
            print('hello')
            #return render(request,'users:indexView')
            return HttpResponseRedirect(reverse('users:indexView'))
           else:
            return render(request,"login.html",{"msg":"用户未激活"})
        else:
          return render(request,'login.html',{"msg":"用户名或密码错误"})

class LogoutView(View):
    #登出功能
    login_url='/login/'
    def get(self,request:HttpRequest):
        logout(request)
        return HttpResponseRedirect(reverse('users:loginView'))