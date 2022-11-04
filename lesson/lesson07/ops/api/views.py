from django.shortcuts import render,redirect
from django.http  import HttpRequest, HttpResponse, JsonResponse
import subprocess



# Create your views here.

'''
def helloView():
    return "hello View"
'''

def helloView(request):
    htmlString='''
    <html>
        <head>
            <title>51reboot</title>
        </head>
        <body>
            <h1>hello View</h1>
        </body>
    </html>
    '''
    return HttpResponse(htmlString)


'''
 parm: ?/args1=1&args2=2
'''
def sumView(request,*args,**kvargs):
    print(request,type(request))
    print("dir request {}".format(dir(request)))
    print("dir request.GET {}".format(dir(request.GET)))
    print("dir request.GET {}".format(request.GET))
    print("request GET.get args1 value  {}".format(request.GET.get('args1')))
    args1 = int(request.GET.get("args1"))
    args2 = int(request.GET.get("args2"))
    svalue = args1+args2 
    print("args1 :{}  args2 : {}  sum :{}".format(args1,args2,svalue))

    return HttpResponse(svalue)

'''CommandView'''
def CommandView(request,*args,**kwargs):
    command=request.GET.get("args")
    cmdres=subprocess.getoutput(command)
    #subprocess.getstatusoutput()
    print("cmd is {},res :{}".format(command,cmdres))
    return HttpResponse(cmdres)

'''登录页面login.html的加载渲染函数'''
def LoginShowView(request,*args,**kvargs):
    print("Login Show View")
    return render(request=request,template_name="login.html",context="Login show view")

'''登录页面逻辑的处理函数'''
def LoginView(request,*args,**kvargs):
    username=request.GET.get("username")
    password=request.GET.get("password")
    print("Login View")
    if username and password:
        userinfo=("test","test")
        if userinfo[0] == username and userinfo[1]==password:
            login_result="login sucess"
        else:
            login_result="login fail"
            #return redirect('api/login_auth/')
    else:
        login_result = "username and password is required"
    return HttpResponse(login_result)   
    
'''登录认证处理'''
def LoginAuthView(request,*args,**kwargs):
    if request.method == "GET":
        return render(request=request,template_name="login.html")
    elif request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print("Login View")
        if username and password:
            userinfo=("test","test")
            if userinfo[0] == username and userinfo[1]==password:
                login_result="login sucess"
            else:
                #login_result="login fail"
                #return redirect('/api/login_auth/')
                return render(request=request,template_name='login.html',context={'msg':'login fail'})
        else:
            login_result = "username and password is required"
        return HttpResponse(login_result)


