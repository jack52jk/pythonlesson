# file operation
'''
open(
file, 
mode='r', 
buffering=-1, 
encoding=None, 
errors=None, 
newline=None, 
closefd=True, 
opener=None
)
    Open file and return a stream.  Raise OSError upon failure.
'''
# 1 open file

from encodings import utf_8
import readline


fd=open("hangdong.txt","w")



# 2 文件操作
st = "1\n 2 \n 3 \n"
d = {"name":"dkfj","age":"dfdjfk"}
fd.write(str(d))


# 3 关闭文件
fd.close()



