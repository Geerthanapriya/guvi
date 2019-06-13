s,e=map(int,input().split())
for i in range (s+1,e):
  sum=0
  temp=i
  while(temp>0):
    a=temp%10
    sum=sum+a**3
    temp=temp//10
  if(i==sum):
    print(i,end=' ')
  
