"""
1 登录认证
2 增删改查和搜索
   2.1 增 add       #add monkey 12 132xxx
   2.2 删 delete    #delete monkey
   2.3 改 update    #update monkey set age = 1
   2.4 查 list      #list
   2.5 搜 find      #find monkey
3. 格式化输出
"""





RESULT=[]
INIT_FAIL_CNT=1
MAX_FAIL_CNT=4
USERINFO = ("hang","hang")
FILED_NAME=["name","age","tel"]

RESULT.append(FILED_NAME)


while INIT_FAIL_CNT<MAX_FAIL_CNT:
    username=input("Please input your username:")
    password=input("Please input your password:")
    if USERINFO[0] == username and USERINFO[1] == password:

        while True:
            fd = open("test.txt","w")
            info = input("Please input UserInfo:")
            info_list = info.split()
            action = info_list[0]
            value = info_list[1:]
            if action == "add":
                #判断新增的数据是否已存在，否则不添加数据
                if value not in RESULT:
                    RESULT.append(value)
                    print("add {} success".format(value))
                else:
                    print("data exist")
            elif action == "delete":
                if value in RESULT:
                    RESULT.remove(value)
                else :
                    print("delete item is not exists ")
                print("delete value is {},after is {}".format(value,RESULT))
            elif action == "update":
                for i in RESULT :
                    #判断用户名
                    if value[0] in i :
                         i[1] = value[1]
                         print("update {},sucess".format(i))
                         break

              
            elif action == "find":
                for i in RESULT:
                    if value[0] in i:
                        print("user {} info is {}".format(value[0],i[1:])) 
            elif action == "list":
                print(RESULT)
                for k,v,z in RESULT:
                    print(" {} {} {}".format(k,v,z))
                print()
            elif action == "exit":
                break
            else:
                print("invaild action")

    else:
        print("username or password error")
        INIT_FAIL_CNT+=1
    

print("GAME OVER.")