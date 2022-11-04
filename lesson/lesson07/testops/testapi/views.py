from django.shortcuts import render
from django.http    import HttpResponse
import subprocess
# Create your views here.

#Hello Views
def HelloViews(request,*args,**kwargs):
    hello = "Hello Views for Django"
    return HttpResponse(hello)


# system cmd  ./testapi/command?cmd=ls
def CommandViews(request,*args,**kwargs):
    cmd = request.GET.get('cmd')
    

    isok,res=subprocess.getstatusoutput(cmd)
    print('cmd is {},status is {},res is {}'.format(cmd,isok,res))
    if isok:
        res = "command is fail"
    return HttpResponse(res)    



#login Views
def LoginViews(request,*args,**kwargs):
    print("-----------------Login Views test--------------")
    return render(request,'login.html')

#login logic 登录逻辑处理函数
def LoginLogicViews(request,*args,**kwargs):
    #print("request dir{}".format(dir(request)) )
    method = request.method
    userinfo = ('test','test')
    result = ""
    if method== "GET":
        username = request.GET.get('username')
        password = request.GET.get('password')
    elif method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    
    if not (username and password):
         result="username or password required"
    elif(userinfo[0]==username and userinfo[1] == password):
        result="login sucess"
    else:
        result = "login fail"


    print("login view form method is {},{}".format(method,username))
    return HttpResponse(result)