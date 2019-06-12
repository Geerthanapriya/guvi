num=input()
num=int(num)
temp=num
a=0
while temp!=0 :
  a=(a*10)+(temp%10)
  temp=temp//10
if(num==a):
  print('yes')
else:
  print('no')
