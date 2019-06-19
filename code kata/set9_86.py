l=list(input())
li=[]
for i in l:
  if i not in li:
    li.append(i)
if(l==li):
  print('Yes')
else:
  print('No')
