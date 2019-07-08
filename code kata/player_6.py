su1,su2=map(str,input().split())
if(len(su1)!=len(su2)):
    print("no")
else :
    s1=[su1.count(i) for i in su1]
    s2=[su2.count(i) for i in su2]
if(s1==s2):
    print("yes")
else:
    print("no")
