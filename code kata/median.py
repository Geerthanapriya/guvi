num=input()
num=int(num)
l=list(map(int,input().split()))
sort=sorted(l)
i = (len(l) - 1) // 2
print(sort[i])
