from collections import deque
import sys
input = sys.stdin.readline

c, r = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(r)]
da = [-1, 0, 1, 0]
db = [0, -1, 0, 1]
d = deque()
for i in range(r):
    for j in range(c):
        if house[i][j] == 1:
            d.append((i, j))

while d:
    a, b = d.popleft()

    for i in range(4):
        na, nb = a + da[i], b + db[i]
        if 0 <= na < r and 0 <= nb < c and house[na][nb] == 0:
            house[na][nb] = house[a][b] + 1
            d.append((na, nb))

cnt0 = 0
m = 0
for i in range(r):
    for j in range(c):
        if house[i][j] > m:
            m = house[i][j]
        if cnt0 == 0 and house[i][j] == 0:
            cnt0 = 1

if cnt0:
    print(-1)
else:
    print(m - 1)