
import copy


with open("/etc/passwd","r") as fd:
    # data = fd.read()
    print(fd.read())
    # datalist = data.split(":")
   # print(datalist)
    for data in fd:
        datalist = data.strip("\n").split(":")
        print("{:<10} {:^5}  {:>30}".format(datalist[0],datalist[2],datalist[4]))

a = {1:{1,23}}
b = a.copy()
b[1].add(3)
print(a,b)

c = copy.deepcopy(a)
a = {1:{1,23}}
c[2]={33}
print(a,id(a))
print(c,id(c))
