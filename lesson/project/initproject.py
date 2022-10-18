'''
用户登录管理系统   user,passwd,tel,man or women
1. 登录认证
       user:hangdong passwd hangdong
2 相关操作
    1) 增  add # add monkey kdfjie  182 man
    2) 删  del # delete monkey
    3) 改  update # update monkey = 2
    4) 查  find # find monkey
3 格式化输出
'''
from prettytable import PrettyTable


username = "hangdong"
password = "hangdong"
RetryCount = 3
count = 0
islogin = False
propmt = {
    "add":"# add monkey kdfjie  182 man",
    "del":" # delete monkey",
    "update":"# update monkey = 2",
    "find":" # find monkey",
    "list":" # list all result",
     "exit":" #program end"
}
Result = []  #存储相关操作的结果
pt = PrettyTable()
#pt.title("userinfo table")
pt.field_names=["name","addr","phone","sex"]


while True:
    
    print("input count is:{}".format(count))
    if count < RetryCount:
        uname = input("please input your username:")
        passwd = input("please input your password:")
        count = count+1
    elif  count >=RetryCount:
        print("input count is out of count;login exit")
        break
    
    print(uname,passwd)
    if  uname == username and passwd == password:
        print("login sucess for username:{}".format(uname))
        islogin = True
    
    print("\n")
    while islogin:
        '''        
        print("add # add monkey kdfjie  182 man")
        print("del # delete monkey")
        print("update # update monkey = 2")
        print("find # find monkey")
        print("list # list all result")
        print("exit #program end")
        '''
        
        for k,v in propmt.items():
            print("op key :{},propmt is:{}".format(k,v))



        data = input("please choose your operater:")
        opdata = data.split()
        op = opdata[0]
        data = opdata[1:]
        
        print(opdata[0],opdata[1:])
        if op == "add":
            Result.append(data)
            print("op is add")
            print(Result)
            pass
        elif op == "del" :
            Result.remove(data)
            
            print("op is del")
            pass
        elif op == "update":
            print("op is delete")
            pass
        elif op == "find":
            print("op is find")
            pass
        elif op == "list":
            pt.add_rows(Result)
            print("op is list")
            print(pt)
            pass
        elif op == "exit":
            exit()
        else:
            print("invaild operater")
   


