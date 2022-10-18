
# 用户管理系统

'''python
1 增加
2 修改
3 删除
4 列出
5 搜索
6 分页
7 退出
8 保存
9 加载

日志
csv
'''



# 标准模块

from prettytable import PrettyTable
import sys
import json


#第三方模块


#全局变量
FILE_NAME = 'user.txt'
RESULT={}
""" RESULT={
        'kk': {'name': 'kk', 'age': '12', 'tel': '132xxx', 'mail': 'djfkd@qq.com'},
        'kk1': {'name': 'kk1', 'age': '12', 'tel': '132xxx', 'mail': 'djfkd@qq.com'},
        'kk2': {'name': 'kk2', 'age': '12', 'tel': '132xxx', 'mail': 'djfkd@qq.com'},
        'kk3': {'name': 'kk3', 'age': '12', 'tel': '132xxx', 'mail': 'djfkd@qq.com'},
        'kk4': {'name': 'kk4', 'age': '12', 'tel': '132xxx', 'mail': 'djfkd@qq.com'},
        'kk5': {'name': 'kk5', 'age': '12', 'tel': '132xxx', 'mail': 'djfkd@qq.com'},
        'kk6': {'name': 'kk6', 'age': '12', 'tel': '132xxx', 'mail': 'djfkd@qq.com'},
        'kk7': {'name': 'kk7', 'age': '12', 'tel': '132xxx', 'mail': 'djfkd@qq.com'},
        'kk8': {'name': 'kk8', 'age': '12', 'tel': '132xxx', 'mail': 'djfkd@qq.com'},
        'kk9': {'name': 'kk9', 'age': '12', 'tel': '132xxx', 'mail': 'djfkd@qq.com'}
        
        } """

def auth(username,password):
    userINFO = ('test','test')
    if userINFO[0] == username and userINFO[1] == password:
        return True
    else:
        return False



def addUser( args ):
    """  
    add monkey1 12  132xxx  monkey1@qq.com
    """
    print(args,type(args))
    userinfolist =args.split()
    if len(userinfolist) != 4:
        return "addUser Fail!"
    username = userinfolist[0]
    print(userinfolist)
 

    if username  in RESULT:
        print("username :{} already exists".format(username))
    else:
        RESULT[username] = {
        'name':username,
        'age':userinfolist[1],
        'tel':userinfolist[2],
        'mail' : userinfolist[3],
        }
        print("add username:{} sucess!".format(username))
    print(RESULT)

""" 
updateUser  monkey1 set age = 20
:parms monkey1  set age = 20
:return 
"""
def updateUser(args):
    print(args)
    userinfoList = args.split()
    if(len(userinfoList) !=5):
        return "UpdateUser failed, args length !=5"

    where = userinfoList[1]
    wherefuhao = userinfoList[3]
    if where != 'set' or  wherefuhao != '=':
        return 'syntax error!.'
    else:
        username = userinfoList[0]
        wherefiled = userinfoList[2]
        updatevalue = userinfoList[4]
        RESULT[username][wherefiled]=updatevalue
    print("update value is {}".format(RESULT))
def deleteUser(args):
    """ 
    delete name
    args name
    return ''
    """
    print(RESULT)
    userinfoList=args.split()
    if len(userinfoList) != 1:
        print("delete user:{}  Fail".format(userinfoList))
  
    username = args
    if username in RESULT:
        RESULT.pop(username)
        print("delete user {} is sucess".format(username))
    else:
        print("username {} not exists".format(username))

    print(RESULT)
""" 
listUser
"""   
def listUser():
    pt = PrettyTable()
    pt.field_names=("name","age","tel","email")
    for k,v in RESULT.items():
        pt.add_row(v.values())
    print(pt)

def findUser(args):
    username = args
    if username in RESULT:
        userinfo = RESULT[username]
        pt = PrettyTable()
        pt.field_names=("name","age","tel","email")
        pt.add_row(list(userinfo.values()))
        print(pt)
    else:
        print("username {} not exists".format(username))

""" 
display page 2 pagesize 5
:param args : page 2 pagesize 5; default pagesize 5;
:return;

"""
def displayUser(args):

    userinfoList=args.split()
    print(len(userinfoList),userinfoList)
    if len(userinfoList) == 2:
        if userinfoList[0] != 'page':
            return 'syntax error.'
        values = [list(v.values()) for k,v in RESULT.items()]

        pageValues = int(userinfoList[1]) -1
        pagesize = 5

        start = pageValues*pagesize
        end = start+pagesize

        print(values[start:end])
        pt = PrettyTable()
        pt.title='user Info'
       
        pt.field_names = ['name','age','tel','email']
        pt.add_rows(values[start:end])
        print(pt,pt.title)

    elif len(userinfoList) == 4:
        if userinfoList[0] == 'page' and userinfoList[2] == 'pagesize':
            values = [list(v.values()) for k,v in RESULT.items()]
            pageValues = int(userinfoList[1])-1
            pagesize = int(userinfoList[3])
            start = pageValues*pagesize
            end = start+pagesize
            pt = PrettyTable()
            pt.field_names=['name','age','tel','email'] 
            
            pt.add_rows(values[start:end])
            print(values[start:end])
            print(pt)
    else:
        return 'syntax error.'


def save():
    """ 
    内存中的文件 写入磁盘
    """
    with open(FILE_NAME,'w') as fd:
        fd.write(json.dumps(RESULT))

def load():
    """  
    读取磁盘数据到内存中
    """
    #v1
   
    with open(FILE_NAME,'r') as fd:
        data = fd.read()
        if not len(data):
            return {}
        return json.loads(data)
    
    
"""     #v2 
    try:
        fd = open(FILE_NAME,'r')
    except Exception as  e:
        pass
    finally:
        fd.close() """

def login():
    while True:
        userinfo = input("please input your userinfo :")
        if len(userinfo) ==0:
            print("invaild input")
        else:
            userinfoList = userinfo.split()
            action = userinfoList[0]
            userinfoString = ' '.join(userinfoList[1:])
            if action == 'add':
                addUser(userinfoString)
            elif action == 'delete':
                deleteUser(userinfoString)
            elif action == 'update':
                updateUser(userinfoString)
            elif action == 'find':
                findUser(userinfoString)
            elif action == 'display':
                displayUser(userinfoString)
            elif action == 'list':
                listUser()
            elif action == 'save':
                save()
            elif action == 'load':
                global RESULT
                RESULT=load()
            elif action == 'logout':
                logout()
            else:
                pass

def logout():
    sys.exit(0)

'''
入口函数
'''

def main():


    """     
            while True:
            userinfo = input("please input UserInfo(name,age,tel,email):")   
            #addUser(userinfo)
            #deleteUser(userinfo)
            #listUser()
            #findUser(userinfo)
            #updateUser(userinfo)
            displayUser(userinfo)
    """
    initFailCount = 0
    maxFailCount=3
    while initFailCount <maxFailCount:
        username = input("Please input your username:")
        password = input("Please input your password:")
        if auth(username,password):
            print("\n\t Welcome user manage system!\n")
            login()
        else:
            print("username or password fail!")
            initFailCount +=1
        


if __name__ == '__main__':
    main()