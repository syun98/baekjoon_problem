n = int(input())
num = list(list(map(int,input().split())) for _ in range(n))

for i in range(1,20):
    for j in range(1,20):
        if [i,j] in num:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()