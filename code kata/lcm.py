num1,num2=map(int,input().split())
def lcm(num1,num2):
  if(num1==0):
    return num2
  return lcm(num2%num1,num1)
print(int((num1*num2)/lcm(num1,num2)))
