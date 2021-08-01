def check(i, j):
    cnt = abs(i) + abs(j)       # 연산 횟수; 1, 2번째 원소의 연산 횟수로 초기화
    arr = []
    arr.append(b[1] + j)
    diff = b[1] + j - b[0] - i  # 공차 == 1, 2번재 원소의 차

    for k in range(2, n):
        if b[k] == arr[k - 2] + diff:
            arr.append(b[k])
        elif b[k] - 1 == arr[k - 2] + diff:
            arr.append(b[k] - 1)
            cnt += 1
        elif b[k] + 1 == arr[k - 2] + diff:
            arr.append(b[k] + 1)
            cnt += 1
        else:               # 배열의 원소 중 하나라도 조건에 해당되지 않으면,
            return False    # 배열은 등차 수열이 아님
    return cnt


n = int(input())
b = list(map(int, input().split()))
result = 100001 # 수열의 최대크기 + 1

if n < 3:       # n이 0,1,2인 경우
    print(0)    # 무조건 등차수열이기 때문에 연산 필요하지 않음
    exit()

for i in range(-1, 2):      # 첫 번째 원소에 연산을 적용할 값
    for j in range(-1, 2):  # 두 번재 원소에 연산을 적용할 값
        temp = check(i, j)
        if temp == False:   # 등차 수열이 만들어 지지 않음
            continue
        else:
            result = min(result, temp)

if result == 100001:    # 등차 수열로 변환이 불가한 경우
    print(-1)
else:
    print(result)
