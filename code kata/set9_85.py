n=input()
l1=[]
l2=[]
for i in range (0,len(n)):
  if(i%2==0):
    l1.insert(i,n[i])
  else:
    l2.insert(i,n[i])
print(''.join(map(str,l1)),end=' ')
print(''.join(map(str,l2)),end=' ')
