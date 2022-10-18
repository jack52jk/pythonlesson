#字典的 遍历 ，查找，更新，删除，增加

from pickle import APPEND
from re import I, L


l1 = ["go","python","C","Java","go","go"]
dt1 = {}

#统计l1 中每项出现的次数

for l in l1:
    #dt1[l] = dt1.get(l,0)+1
    if l not in dt1:
        dt1[l] = 1
    else:
        dt1[l] = dt1[l] +1
    print("key is {},value is :{}".format(l,dt1[l]))

# 把字典的key转换为列表,字典的值也转换为列表
keylist = list(dt1.keys())
vallist = list(dt1.values())

print("key : {}, val : {}".format(keylist,vallist))

#  1) 遍历 dict
for key in dt1:
    print("key is :{},val :{}".format(key,dt1[key]))

for k,v in dt1.items():
    print(k,v)

# 2) 增加 dict
dt1["MySQL"] = 5

print(dt1)

# 使用列表增加元素
listdictkey = list(dt1.keys())
listdictvalue = list(dt1.values()) 
listdictkey.append("MYSQL2")
listdictvalue.append(5)



print("dict key is :{},val is {}".format(listdictkey,listdictvalue))


dt2={listdictkey[i]:listdictvalue[i] for i in range(0,len(listdictkey))}   #遍历的list 太大，会造成内存暴增现象
# dt2 = dict(zip(listdictkey,listdictvalue))

print("根据list类型的key和值增加新的dict元素,字典为: ")
print(dt2)


# 3) 修改 dict
dt1["MySQL"] = 3

print(dt1)


# 3) 删除 dict
print(dt1.pop("go",None))
print(dt1)
#4) 清空dict
dt1.clear()
print(dt1)


dt3 = {k:v for v,k in dt2.items()}
print(dt3)


