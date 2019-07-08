sa1,ke1=map(int,input().split())
sd1=[]
for i in range(sa1+1,ke1+1):
    for x in range(2,i):
       if(i%x==0): 
           break
    else:
         sd1.append(x)
print(len(sd1)+1)
