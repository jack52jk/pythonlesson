"""
def fun(arg1,arg2,arg3):
    pass
    return
"""

import os
from time import sleep
for dirname,dirpath,filename in os.walk("/home/huaplus"):
    print(dirname,dirpath,filename)
    sleep(10)

