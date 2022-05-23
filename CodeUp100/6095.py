plate = [[0 for _ in range(19)] for _ in range(19)]

n = int(input())
for _ in range(n):
    i, j = map(int, input().split())
    plate[i-1][j-1] = 1

for i in range(19):
    for j in range(19):
        print(plate[i][j], end=' ')
    print()