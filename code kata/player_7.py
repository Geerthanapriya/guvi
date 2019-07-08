n1=list(input())
for i in range(0,len(n1),2):
  n1[i],n1[i+1]=n1[i+1],n1[i]
n2=''.join(n1)
print(n2)
