import math
num1,num2=map(int,input().split())
number=num1*num2
root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print('yes')
else:
    print('no')
