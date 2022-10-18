from random import Random, random, uniform


tp1 = (1,2,3,1)
tp2 = tuple(range(5))
print(type(tp1),type(tp2),tp2)

print(dir(tuple))

print(tp1.count(2))
print(tp1.index(1))
print(dir(dict))

l = [1,2,3,4]
ltmp = [5,6]
print(type(l))
print(dir(l))
l.append(({"k":"v"}))
print(l)
#l.clear()
#print(l)
l1 = l.copy()
print(l,l1)
num = l.count(1)
print(num,l)
l.extend(ltmp)
print(l)
print(l.index(5))


l.insert(2,5)
print(l)

l.pop(2)
print(l)

l.remove(1)
print(l)
l.reverse()
print(l)
#l.sort()
#print(l)

for i,v in enumerate(l):
    print(i,v)

