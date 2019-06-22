num=int(input())
li=list(map(int,input().split()))
for i in range (len(li)):
  if(li[i]>li[i+1]):
    break
print(i)
