num=input()
num=int(num)
Count = 0
while(num > 0):
    num = num // 10
    Count = Count + 1
print(Count)
