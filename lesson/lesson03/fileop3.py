
import json


fd = open("hang.txt","r")

context = fd.read()
print(json.loads(context),type(json.loads(context)))