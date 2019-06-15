num1,num2=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in l:
  if(i==num2):
    count=count+1
print(count)
