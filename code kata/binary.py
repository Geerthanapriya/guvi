numeric=input()
a=0
for i in numeric:
  if i=='0' or i=='1':
    a=a+1
  else:
    break
if a==len(numeric):
  print('yes')
else:
  print('no')
