n = int(input())
num = list(map(int,input().split()))

result = num[0]
for i in num:
    result = min(i,result)
print(result)