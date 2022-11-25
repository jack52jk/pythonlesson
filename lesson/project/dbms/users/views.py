from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpRequest, HttpResponseRedirect, QueryDict

# Create your views here.

# class UsersViews(View):
#     def listUserView( request:HttpRequest):
#         return render(request,template_name='users/userslist.html')
    

# def indexView(request:HttpRequest,**kwargs):
#     return render(request,template_name="index.html")


#首页
class IndexView(View):
    def get(self,requeset:HttpRequest):
        return render(requeset,'login.html')

class LoginView(View):
#登录功能
    def post(self,request:HttpRequest):
        username = QueryDict( request.body).dict().get('username')
        password = QueryDict(request.body).dict().get('password')
        print('username is {},password is {}'.format(username,password))
        #users = UserProfile.objects.filter(username = username)
        users = authenticate(username=username,password=password)
        print ("users is {},{}".format(users,type(users)))
        if users:
           if users.is_active:
            #默认为当前用户创建session
            login(request,users)  #生成登录成功后访问任何页面的认证
            print('hello')
            #登录成功使用命名空间跳转到首页
            return render(request,'index.html')
        return render(request,'login.html')
    
class LogoutView(View):
    #登出功能
    login_url='/login/'
    def get(self,request:HttpRequest):
        logout(request)
        return HttpResponseRedirect(reverse('users:loginView'))

#登录成功后的首页    
class Index(View):
    def get(self,request:HttpRequest):
        return HttpResponse(request,'index.html')
    

class UserView(View):
    def get(self,request:HttpRequest):
        return render(request,'users/list.html')