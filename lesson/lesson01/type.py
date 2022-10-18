
from tokenize import Double


ty1 = 1.920
print(type(ty1))

s1 = '''echo "sfdfd"'''
s2 = """ select ui where \\\${ty1}"""

print(s1,s2,type(s1))

print(True and False or True)

print(type(ty1),ty1)