from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpRequest, HttpResponseRedirect, QueryDict
from users import models
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
        user=models.User.objects.all()
        users = {"users":user}
       # print("user is {}".format(users))
        return render(request,'users/list.html',users)

#获取用户详细信息
    def getView(request:HttpRequest):
        print("request is {}".format(request))
        uid = int(request.GET.get("id"))
        
        udetail = models.User.objects.filter(id=uid)
         #print("udetail is {}, {} ".format(udetail,udetail[0].username))
        #print("user is {}".format(user))
        users = {"users":udetail}
        return render(request,'users/detail.html',users)

#获取用户详细信息
    def editView(request:HttpRequest):
        print("request is {}".format(request))
        uid = int(request.GET.get("id"))
        
        udetail = models.User.objects.filter(id=uid)
         #print("udetail is {}, {} ".format(udetail,udetail[0].username))
        #print("user is {}".format(user))
        users = {"users":udetail}
        return render(request,'users/edit.html',users)
    #保存修改得信息
    def editSaveView(request:HttpRequest):
        print("request is {}  body {}".format(request,request.body))
        id = int(QueryDict(request.body).dict().get('id'))
        username = QueryDict(request.body).dict().get('username')
        password = QueryDict(request.body).dict().get('password')
        age = QueryDict(request.body).dict().get('age')
        
        userobject = models.User.objects.filter(id=id)
        #userobject[0].username=username
        # userobject[0].password = password
        # userobject[0].age  = age
        userobject.update(username=username,password=password,age=age) 
        print("id,uname,passwd {},{},{}".format(id,userobject[0].username,username))
        
        
        # sql = "update user set username={},password={},age={} where id={};".format(username,password,age,id)
        # models.User.objects.raw(sql)
        return HttpResponseRedirect(reverse("users:list"))
    
    #删除用户信息
    def deleteById(request:HttpRequest):
        id = int(request.GET.get("id"))
        print("id is {},{}".format(id,type(id)))
        delobject=models.User.objects.filter(id=id)
        res=delobject.delete()
        print(res)
        return HttpResponseRedirect(reverse("users:list"))








class AddView(View):
      def get(self,request:HttpRequest):
        return render(request,'users/add.html')
    
      def post(self,request:HttpRequest):
        print("add save {} {}".format(self.post ,request.body))
        username = QueryDict(request.body).dict().get('username')
        password = QueryDict(request.body).dict().get('password')
        age      = QueryDict(request.body).dict().get('age')
        print("username {} password {} age {}".format(username,password,age))
        models.User.save()
        return HttpResponseRedirect(reverse("users:add"))

class AddSaveView(View):
      def post(self,request:HttpRequest):
        print("add save {} {}".format(self.post ,request.body))
        username = QueryDict(request.body).dict().get('username')
        password = QueryDict(request.body).dict().get('password')
        age      = QueryDict(request.body).dict().get('age')
        print("username : {} ,password :{} ,age :{}".format(username,password,age))
        u = models.User(username=username,password=password,age=age)
        u.save()
        print(u)
        return HttpResponseRedirect(reverse("users:add"))