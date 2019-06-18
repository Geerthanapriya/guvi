numeric=input()
a=[int(x) for x in numeric]
for i in numeric:
    if(int(i)%2)!=0:
        print(i,end=" ")
