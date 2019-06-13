n=int(input())
li=list(map(int,input().split()))
li.sort()
for i in range (0,len(li)):
  print(li[i],end=' ')
