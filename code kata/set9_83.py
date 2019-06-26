num=input()
for i in num:
  if(i=='/'):
    s=num.split('/')
    print(int(int(s[0]))/(int(s[1])))
  elif(i=='%'):
    s=num.split('%')
    print(int(int(s[0]))%(int(s[1])))
