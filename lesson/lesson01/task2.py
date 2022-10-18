
score = input("please enter your score :")
res = ''
if int(score) >= 90:
    res='A'
elif int(score) <90 and int(score) >=80:
    res = 'B'
elif int(score) <80 and int(score) >=70:
    res='C'
elif int(score) <70 and int(score) >=60:
    res='D'
else:
    res='E'

print("your score is <",score,">,get<",res,">.")
print("your score is <{}>,get <{}>.".format(score,res))