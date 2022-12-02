from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,QueryDict,HttpResponseRedirect
from django.urls import reverse
from users.models import Users
from users.views import listView

# Create your views here.

# def index(request):
#     return HttpResponse("<p> Hello World,Hello Django</p>")

# def index(request:HttpRequest):   #request:HttpRequest  注解 request参数的类型为HttpRequest类型
#     print(request)
#     #设置默认值的方式 获取数据更优雅
#     year =request.GET.get("year","2022")
#     #直接获取数据,没有传会报错,不建议
#     month = request.GET['month']
#     return HttpResponse("year is %s,month is %s" %(year,month))

#位置参数的处理函数
# def index(request:HttpRequest,year=2022,month=1):   #request:HttpRequest  注解 request参数的类型为HttpRequest类型
#     return HttpResponse("year is %s,month is %s" %(year,month))

# # #关键词传参的处理函数
#请求参数接收,默认为GET请求,通过method判断POST请求
# def index(request:HttpRequest,**kwargs):   #request:HttpRequest  注解 request参数的类型为HttpRequest类型
#     print(kwargs)
#     print("request scheme {}".format(request.scheme))   #http
#     print("request headers {}".format(request.headers)) #{'Content-Length': '18', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': '127.0.0.1:8000', 'User-Agent': 'curl/7.68.0', 'Accept': '*/*'}
#     print("request path {}".format(request.path))       # /hello/hello/
#     print("request META {}".format(request.META))       # {'REMOTE_ADDR': '127.0.0.1','HTTP_HOST': '127.0.0.1:8000'...}

#     #直接获取数据,没有传会报错,不建议
#     if(request.method=="POST"):
#         print(request.method) #POST
#         print(request.body)    #b'year=2022&month=11'
#         print(request.POST)   #<QueryDict: {'year': ['2022'], 'month': ['11']}> 获取相应信息中post发送的数据通过此方法request.POST.getlist(key)
#         print(QueryDict(request.body).dict())  #{'year': '2022', 'month': '11'}
#         print(type(request.POST))
#         data = request.GET
#         print("data is {},type {}".format(data,type(data)))
#         year =data.get("year","2022")
#         month = data.get('month',11)
#     else:
#         print("request method {}".format(request.method))
#         print("request body {}".format(request.body))
#         print("request encoding {}".format(request.encoding))
#         print("request GET {}".format(request.GET)) #<QueryDict: {'year': ['2022'], 'month': ['11']}> 获取相应信息中get发送的数据通过此方法request.GET.getlist('key') 适用于复选框场景
#         data = request.GET
#         year =data.get("year","2022")
#         month = data.get('month',11)
#     return HttpResponse("year is %s,month is %s" %(year,month))

# def index(request:HttpRequest,month=1,year=2022):   #request:HttpRequest  注解 request参数的类型为HttpRequest类型
#     return HttpResponse("year is %s,month is %s" %(year,month))


def index(request:HttpRequest,**kwargs):
    print(request.headers)
    print(type(request.body))
    
    title='test'            #普通变量   首页
    books=['java','c','python','c++']  #列表变量  列表页
    people={'name':'kk','age':18,'sex':'man'} #字典变量, 详情页
    l = {
        "people":people,
        "title":title,
        'books':books
    }
    return render(request,'hello/index.html',l)

def test(request:HttpRequest):
    product=[{'pid':1,'name':'dot'},{'pid':2,'name':'fush'},{'pid':3,'name':'dog'},{'pid':4,'name':'pig'}]
    dt={'product':product}
    return render(request,'hello/form.html',dt)

def loginView(request:HttpRequest):
    data=''
     
    if request.method == 'POST':
        print(QueryDict(request.body).dict())
     
        username=QueryDict(request.body).dict().get('username')
        password=QueryDict(request.body).dict().get('password')
        users = Users.objects.get()
        print("users is {}".format(type(users)))
        if username == 'admin' and password == 'admin':
            data = 'login sucess'
            #return HttpResponseRedirect('/hello/hello/')
            return HttpResponseRedirect(reverse('hello:index'))
        else:
            data= 'your username or password error! Please again'
    dt = {'data':data}
    return render(request,'hello/login.html',context=dt)


#遍历用户信息
def listView(request:HttpRequest):
    # user = [
    #     {'username':'test1','username_en':'jack01','age':1},
    #     {'username':'test2','username_en':'jack02','age':2},
    #     {'username':'test3','username_en':'jack03','age':3},
    # ]
    user = Users.objects.all()

    return render(request,'hello/list.html',{'user':user})

def indexView(request:HttpRequest):
    return render(request,'hello/index.html')