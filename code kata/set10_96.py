A,D,N=(map(int,input().split()))
sum=0
for i in range(1,N+1): 
    sum=sum+(A+(i-1)*D)
print(sum)
