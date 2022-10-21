import xml.etree.ElementTree as et

tree = et.parse("schema.xml")

for n in tree.iter():
    print(n.keys())




s = 'abc'
c = '.'
print(c.join(s))

# print(s.count('d'))

# print(s,c)