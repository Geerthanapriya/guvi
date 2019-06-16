nu=int(input())
if(nu==1):
  print('no')
elif(nu==2):
  print('yes')
else:
  for x in range(2,nu):
    if(nu%x)==0:
      print('no')
      break
  else:
    print('yes')
