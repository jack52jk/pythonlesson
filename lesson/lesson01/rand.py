
""" 
猜字谜游戏,根据随机产生的数字,进行6次猜测,猜中输出 中奖,否则输出 感谢参与
"""
from random import Random, randint


resint = Random.randint(1,100)
isbreak = False

for i in range(6):
    num = input("please input num : ")
    if resint == int(num):
        print("恭喜 中奖")
        isbreak=True
        break
    
if not isbreak :
    print("谢谢参与")
print("谜底数:{}".format(resint))