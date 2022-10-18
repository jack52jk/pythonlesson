

# 1 打开文件
fd = open("/etc/passwd","r")


# 2 文件操作

data = fd.readline()

print(data)
#3 关闭文件

fd.close()
