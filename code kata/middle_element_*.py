r=list(input())
if len(r)%2==0:
    r[int(len(r)/2)] ='*'
    r[int(len(r)/2)-1]='*'
else:
    r[int(len(r)/2)] ='*'
for iui in range(0,len(r)):
    print(r[iui],end='')
