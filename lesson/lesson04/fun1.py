import pymysql

pymysql.connect
from re import S


def f1():
    a=1
    b=2
    return a+b,True

s = f1()
print(s,type(s))


def optv(a,b,*boot,**webroot):
    print(a)
    print(b)
    print("reboot:{},{}".format(boot,type(boot)))
   
    print("webroot:{},{}".format(webroot,type(webroot)))


optv(1,2,3,4,5,6,7,8,name="vale",age=20)    



def f4(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


k = [4,5,6]
kw = {"name":"fewe","age":"23"}

f4(1,2,3)
f4(1,2,3,k)
f4(1,2,3,k,kw)
f4(1,2,3,*k,**kw)
