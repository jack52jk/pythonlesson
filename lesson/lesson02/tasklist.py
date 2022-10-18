
# 打印列表中的最大数字
#[5,12,42,4,2,10,25]
l = [5,12,42,4,2,10,25]
maxnum = -1 

for num in l:
    if num > maxnum:
        maxnum = num
print("列表:{} 中的最大数字是:{}".format(l,maxnum))
print()
print()

#移动列表的最大数字到最后
#源列表: [5,12,42,2,5,19]
#目标列表: [5,12,2,5,19,42]
srclist = [5,12,42,2,5,19]
srclen = len(srclist)
maxindex = 0
i = 0
print("源列表为:{}".format(srclist))
while i < srclen:
    if srclist[maxindex] < srclist[i] :
        maxindex = i
        #print(maxindex)
    i = i+1
srclist.append(srclist.pop(maxindex))
print("目标列表为:{}".format(srclist))

#求两个列表中重复的元素的列表
#[1,2,5,7,11]
#[2,15,3,7]

l1 = [1,2,5,7,11]
l2 = [2,15,3,7,1,11,55,2]
l = []

l1len = len(l1)
l2len = len(l2)

if l1len > l2len:
    for lval in l2:
        if lval in l1:
            l.append(lval) 
else:
    for lval in l1:
        if lval in l2:
            l.append(lval)

print("list l1:{} and l2:{} 的交集为:{}".format(l1,l2,l))


#字符串与列表的有序转换
str1 = "9876543210"
desstr1 = ""
sort1 = []

for x in str1:
    sort1.append(x)
print(sort1)
sort1.sort()
print(sort1)

for x in sort1:
    desstr1 += x

print("排序前的字符串为:{},排序后的字符串为:{}".format(str1,desstr1))

ll1 = [1,2,3,4,5]
