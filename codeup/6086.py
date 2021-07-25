n = int(input())
sum = 0

for i in range(1,100000001):
    sum += i
    if sum >= n:
        break
print(sum)