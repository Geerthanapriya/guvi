num = int(input())
n1=0
n2=1
for i in range(1, num+1):
   if(i<=1):
      t=i
   else:
    t=n1+n2
    n1=n2
    n2=t
   print(t,end=' ')
