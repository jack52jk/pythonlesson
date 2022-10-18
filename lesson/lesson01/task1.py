
name = input("Please input your name:")
age = input("Please input your age:")
sex = input("Please input your sex:")
isin = False

if int(age) > 18 :
    isin=True
if isin:
    print("你的名字:",name," 你的年龄:",age,"你的性别:" ,sex,"可以进入",".")
else:
    print("你的名字:",name," 你的年龄:",age,"你的性别:" ,sex,"不可以进入",".")