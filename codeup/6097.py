h, w = map(int, input().split())
n = int(input())
grid = [list(0 for _ in range(w)) for _ in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if d == 0:
        for j in range(l):
            grid[x][y + j] = 1
    else:
        for j in range(l):
            grid[x + j][y] = 1

for i in range(h):
    print(*grid[i])
