


UserInfo = ('test','test')
UserInfoList=[]


def authentication(username,password):
    if UserInfo[0] == username and UserInfo[1] == password:
        return 'login sucess',True
    else:
        return 'login fail',False
# add info to list
def addInfo(info):
    UserInfoList.append(info)

islogin = authentication('dfjkd','dfjke')

print(islogin)

dt = {'e':2,'a':3,'b':1}
f=lambda x,y:x+y
print(f(1,2))
tt = dt.items()
print(dt.items(),type(tt))

ss = sorted(dt.items(),key=lambda x:x[0])
print(ss)