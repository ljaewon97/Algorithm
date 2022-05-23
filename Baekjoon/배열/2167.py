# 2차원 배열의 합

N, M = map(int, input().split())

arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    sum = 0
    for p in range(i-1, x):
        for q in range(j-1, y):
            sum += arr[p][q]

    print(sum)