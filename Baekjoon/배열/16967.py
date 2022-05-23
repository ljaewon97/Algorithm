# 배열 복원하기

H, W, X, Y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H+X)]

A = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H-X):
    for j in range(W-Y):
        arr[i+X][j+Y] -= arr[i][j]

for i in range(H):
    for j in range(W):
        print(arr[i][j], end=' ')
    print()