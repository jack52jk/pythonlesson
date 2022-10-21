
'''
user manage system for function version

1 add monkey 12 132xxx monk@qq.com
2 update monkey set age = 20
3 delete monkey
4 find monkey
5 page monkey
'''


import sys
import prettytable
import json


#RESULT = {}
FILE_NAME = 'usermfun1.txt'
RESULT = {'monkey1': {'name': 'monkey1', 'age': 12, 'tel': '132xxx', 'email': 'monkey1@qq.com'}, 'monkey10': {'name': 'monkey10', 'age': 10, 'tel': '1310xx', 'email': 'monkey10@qq.com'}, 'monkey11': {'name': 'monkey11', 'age': 11, 'tel': '1311xx', 'email': 'monkey11@qq.com'}, 'monkey12': {'name': 'monkey12', 'age': 12, 'tel': '1312xx', 'email': 'monkey12@qq.com'}, 'monkey13': {'name': 'monkey13', 'age': 13, 'tel': '1313xx', 'email': 'monkey13@qq.com'}, 'monkey14': {'name': 'monkey14', 'age': 14, 'tel': '1314xx', 'email': 'monkey14@qq.com'}, 'monkey15': {'name': 'monkey15', 'age': 15, 'tel': '1315xx', 'email': 'monkey15@qq.com'}, 'monkey16': {'name': 'monkey16', 'age': 16, 'tel': '1316xx', 'email': 'monkey16@qq.com'}, 'monkey17': {'name': 'monkey17', 'age': 17, 'tel': '1317xx', 'email': 'monkey17@qq.com'}, 'monkey18': {'name': 'monkey18', 'age': 18, 'tel': '1318xx', 'email': 'monkey18@qq.com'}, 'monkey19': {'name': 'monkey19', 'age': 19, 'tel': '1319xx', 'email': 'monkey19@qq.com'}}
USERINFO=('test','test')


'''
add monkey1 12 132xxx monk@qq.com
:param 
return ;
'''
def add(userinfo):
    userinfoList = userinfo.split()
    if(len(userinfoList) != 4):
        return "add userinfo fail",False
    username = userinfoList[0]
    age = int(userinfoList[1])
    tel = userinfoList[2]
    email = userinfoList[3]
    #判断用户信息是否已存在
    if username in RESULT:
        print("username {} already exits".format(username))
        return "username {} already exits".format(username),False
    else:
        RESULT[username] = {
            'name':username,
            'age':age,
            'tel':tel,
            'email':email
        }
        return "add userinfo sucess",False
    print(RESULT)


'''
update monkey1 set age = 12
:param monkey1 set age = 12
return ;
'''
def update(userinfo):
    userinfolist = userinfo.split()
    if(len(userinfolist)!=5):
        print("update user fail")
        return "update user fail",False
    if userinfolist[1] == 'set' and userinfolist[3] == '=':
        usernamekey = userinfolist[0]
        updatekey = userinfolist[2]
        updatevalue = userinfolist[4]
        RESULT[usernamekey][updatekey] = updatevalue
        return "update user sucess",True
    else:
        print("update syntax error")
        return "update syntax error",False
    print(RESULT)

'''
delete monkey1
:param monkey1 set age = 12
return ;
'''
def delete(userinfo):
    userinfolist = userinfo.split()
    if(len(userinfolist) !=1):
        print("input userinfo error")
        return "input userinfo error",False
    username = userinfolist[0]
    if username not in RESULT:
        print("username {} not exists".format(username))
        return "username {} not exists".format(username),False
    else:
        del RESULT[username]
        return "delete username {} info sucess".format(username),True
    print(RESULT)

'''
:param find monkey1 
return userinfo;
'''
def find(userinfo):
    userinfolist = userinfo.split()
    if(len(userinfolist) != 1 ):
        print("find userinfo error")
        return "find userinfo error" ,False
    username=userinfolist[0]
    if username in RESULT:
        print("username :{} userinfo : {}".format(username,RESULT[username]))
        pt = prettytable.PrettyTable()
        pt.field_names=('name','age','tel','email')
        # dv = list(RESULT[username].values())
        # print(dv,type(dv),list(dv))
        pt.add_row(list(RESULT[username].values()))
        
        print(pt)
        return RESULT[username],True
    else:
        print("username {} not exists".format(username))
        return {},True

'''
page 2 pagesize 2
:param  monkey1 
return userinfo;
'''
def page(userinfo):
    userinfolist = userinfo.split()
    pagelist = []
    if(len(userinfolist) == 2 ):
        pagesize = 5
        pagev = int(userinfolist[1]) -1
        startV = pagesize*pagev
        endV = startV+pagesize
        RESULTlist = [v.values()  for k,v in RESULT.items()]
        pagelist = RESULTlist[startV:endV]
        pt = prettytable.PrettyTable()
        FILED_NAME=('name','age','tel','email')
        pt.field_names=FILED_NAME
        pt.add_rows(pagelist)
        print(pt)
    elif(len(userinfolist) == 4) :
        pagesize = int(userinfolist[3])
        pagev = int(userinfolist[1])-1
        startv = pagev*pagesize        
        endv = startv + pagesize
        RESULTlist = [v.values() for k,v in RESULT.items()]
        pagelist = RESULTlist[startv:endv]
        pt = prettytable.PrettyTable()
        FILED_NAME=('name','age','tel','email')
        pt.field_names=FILED_NAME
        pt.add_rows(pagelist)
        print(pt)
    else:
        print("page syntax error!")


'''
list userinfo
'''
def listUser():
    if(len(RESULT) ==0):
          return {}
    listvalue = [v.values() for k,v in RESULT.items()]
    
    pt = prettytable.PrettyTable()
    pt.field_names = ('name','age','tel','email')
    pt.add_rows(listvalue)
    print(pt)

'''
logout system
'''
def logout():
    sys.exit(0)
    #sys.exit(1)

'''
把内存数据保存在磁盘
'''
def save():
    with open(FILE_NAME,'w') as fd:
        fd.write(json.dumps(RESULT))

'''
从文件中加载数据到内存变量中
'''
def load():
    with open(FILE_NAME,'r') as fd:
        RESULT = json.loads(fd.read())
'''验证用户名和密码'''
def auth(username,password):
    if USERINFO[0] == username and USERINFO[1] == password:
        return True
    else:     
        return False
def operate():
    while True:
        print("choose operater with username:")
        print("\tadd userinfo")
        print("\tupdate userinfo")
        print("\tdelete userinfo")
        print("\tfind userinfo")
        print("\tpage userinfo")
        print("\tlist userinfo")
        print("\tsave userinfo")
        print("\tload userinfo")
        print("\trelogin")
        print("\tlogout")
        operate = input("Please input your operater:")
        if operate == 'add':
            userinfo = input("Please input userinfo(name,age,tel,email):")
            add(userinfo)
        elif operate == 'update':
            userinfo = input("Please input update userinfo(eg  kk set age = 20):")
            update(userinfo)
        elif operate == 'delete':
            userinfo = input("Please input delete userinfo(eg  kk):")
            delete(userinfo)
        elif operate == 'find':
            userinfo = input("Please input find userinfo(eg find kk):")
            find(userinfo)
        elif operate == 'page':
            userinfo = input("Please input page userinfo(eg page 2 or page 2 pagesize 2):")
            page(userinfo)
        elif operate == 'list':
            listUser()
        elif operate == 'save':
            save()
        elif operate == 'load':
            load()
        elif operate == 'relogin':
            login()
        elif operate == 'logout':
            logout()
        else:
            print("invaild input operate")

'''login function'''
def login():
    INIT_COUNT=0
    MAX_COUNT=3
    while INIT_COUNT < MAX_COUNT:
        username = input("Please input Username:")
        password = input("Please input Password:")
        isok = auth(username,password)
        print(isok)
        if isok:
            print('login sucess')
            print("\n\t Welcome User Manager System\n")
            operate()
        else:
            print('username or password error')
        INIT_COUNT +=1
    print("login fail")

'''入口函数'''
def main():
    login()
#def main():
    #while True:
        # for i in range(10,20):
        #     userinfo1 = "monkey{} {} 13{}xx monkey{}@qq.com".format(i,i,i,i)
        #     #print(userinfo1)
        #     userinfo = str(userinfo1)
        #     add(userinfo)
        #userinfo = input("Please input userinfo(name,age,tel,email):")
        #add(userinfo)
        #update(userinfo)
        #listUser()
        # userinfo = input("Please input userinfo(name,age,tel,email):")
        # page(userinfo)
       
        #delete(userinfo)
        #find(userinfo)
        #save()
        # load()
        # listUser()


if __name__ == '__main__':
    main()