import threading
import time

def aws_r():
    print("aws rr")
    time.sleep(5)

def aws_c():
    print("aws c")
    time.sleep(5)

def ali_c():
    print("ali c")
    time.sleep(5)

th1 = threading.Thread(target=aws_r,name="aws r")
th2 = threading.Thread(target=aws_c,name="aws c")
th3 = threading.Thread(target=ali_c,name="ali c")

th = [th1,th2,th3]

for t in th:
    t.start()
