plate = []

for _ in range(19):
    temp = list(map(int, input().split()))
    plate.append(temp)

N = int(input())

for _ in range(N):
    m, n = map(int, input().split())
    for i in range(19):
        if plate[m-1][i] == 0:
            plate[m-1][i] = 1
        elif plate[m-1][i] == 1:
            plate[m-1][i] = 0
        if plate[i][n-1] == 0:
            plate[i][n-1] = 1
        elif plate[i][n-1] == 1:
            plate[i][n-1] = 0

for i in range(19):
    for j in range(19):
        print(plate[i][j], end=' ')
    print()