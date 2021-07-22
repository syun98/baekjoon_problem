n = int(input())
num = [int(x) for x in input().split()]
result = []

first_value = num[0]
max_pow = 0

# 첫번째 값 찾기
for i in range(n):
    temp = num[i]
    pow = 0
    while temp % 3 == 0:
        temp //= 3
        pow += 1
    if (pow > max_pow) or (pow == max_pow and num[i] < first_value):
        max_pow = pow
        first_value = num[i]

result.append(first_value)

# 다음 순서인 수 찾기
for i in range(n):
    if result[-1] * 2 in num:
        result.append(result[-1] * 2)
        continue
    if result[-1] % 3 == 0 and result[-1] // 3 in num:
        result.append(result[-1] // 3)
        continue
    break

if len(result) == n:
    print(*result)