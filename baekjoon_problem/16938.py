import sys
from itertools import combinations

n, l, r, x = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
result = 0

a.sort()

for i in range(n - 1):
    for j in range(n - 1, i, -1):
        if a[j] - a[i] >= x:
            for k in range(j - i):
                for m in combinations(a[i + 1:j], k):
                    sum = a[i] + a[j]
                    for item in m:
                        sum += item
                    if l <= sum <= r:
                        result += 1

print(result)
