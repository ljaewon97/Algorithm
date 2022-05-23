h, w = map(int, input().split())
n = int(input())
plate = [[0 for _ in range(w)] for _ in range(h)]

for _ in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(y, y+l):
            plate[x-1][i-1] = 1
    if d == 1:
        for i in range(x, x+l):
            plate[i-1][y-1] = 1

for i in range(h):
    for j in range(w):
        print(plate[i][j], end=' ')
    print()