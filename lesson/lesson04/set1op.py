
from re import S
dt = {"key":"value"}
lst = ['a','b','c','d']
tup = (7,8,9,'a','c')
print(type(dt),type(lst),type(tup))

s = {1,2,3,4,5}
print(type(s))
print(dir(s))

# s.add method
s.add("dfsdaf")
s.add(3.21)
s.add(False)
s.add(tup)
print("set add is{}".format(s))
# s.pop method
print("set pop is :{},set :{}".format(s.pop(),s))




#s.clear 

#print("set clear method is :{},{}".format(s.clear(),s))

#s.copy
#s1 = s.copy()

#print("copy set is {},{}".format(s1,s))
#s.difference
s2 = {1, 2, 3, 4, 5}

#s3 = s.difference(s2,{1,2,"cdf"})
#print(s3)

#s.difference_update
#print("src set is :{},diff set :{},differupdate is {}".format(s,s2,s.difference_update(s2)))

#set discard
#print(s)
#print("src {} ,discard element :{} ,discard :{} ".format(s,s,s.discard("abv")))

#s5 = s.intersection_update({1,88})
#print(s5,s)
s6=s.isdisjoint({2,88})
print(s6,s)

s7 = s2.issubset(s)
print(s7,s,s2)

s8 = s.issuperset(s2)
print(s8,s)


s9 = s2.symmetric_difference(s)
print(s9)

s9.symmetric_difference_update(s)
print(s9,s)
s9.add(100)
s11 = {"jkk"}
s10= s.update(s9,s11)

print(s9,s10,s)


print(sum(range(100)))

