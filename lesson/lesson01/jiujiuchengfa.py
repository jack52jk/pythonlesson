""" 
九九乘法表
1 * 1 = 1
 """


for i in range(1,12):
    for j in range(1,i+1):
                        # :<字段在可用空间内左对齐
        print("{}*{} = {:<}".format(j,i,i*j),end="   ")
    print("")
