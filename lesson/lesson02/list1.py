
ll = ['a','z','b']
print(ll)
ll[1] = 3
print(ll)

#列表追加元素 在list 末尾追加元素
ll.append(5.64)  
print(ll.count("a"),ll)

#遍历list
for li in ll:
    print(li)
# list的pop方法从最尾部移除元素
print(ll.pop(1),ll)

l1 = [["name","age","11"],["dfd","evdas","12"]]
for i in l1:
    if "name" in i:
        l1.remove(i)
print(l1)