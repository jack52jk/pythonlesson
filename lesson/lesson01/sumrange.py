
sum = 0 
while True:
    num = input("[Debug]please input num :".format(sum))
    if int(num) == 0:
        break;
    else:
        sum = sum + int(num)

print("range num sum is {}".format(sum))