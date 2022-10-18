

import json
from tkinter import E


fd = open("hang.txt","w")

try:
    data = [
        ["name","age","sex"],
        ["dkfj",12,1],
        ["dfkdjf",33,0]
    ]
    data1 = {"name":11,"age":12}
    print(json.dumps(data))
    fd.write(json.dumps(data))
    fd.write("\n")
    fd.write(json.dumps(data1))
except Exception as e:
        print("write file error:{}".format(e))
finally:
    fd.close()


