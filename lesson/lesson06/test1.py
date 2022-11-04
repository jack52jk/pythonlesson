
from textwrap import wrap


# ok = True
# if ok :
#     i = "baidu"
# print(i)

# for j in range(5):
#     age = j
# print(age)



def decorate(func):
     def wrap():
        print("link -----------")
        i = 10
        func()
     return wrap

     
@decorate
def f1():
    #print("------")
    with open("/etc/passwd",'r') as fd:
        print(fd.read())
    print(i)

f1()
