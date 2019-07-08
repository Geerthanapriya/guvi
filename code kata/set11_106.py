n1,n2=map(int,input().split())
l=input().split()
l1=[]
for i in l:
  if(int(i)%2!=0):
    l1.append(i);
print(l1[n2-1])
