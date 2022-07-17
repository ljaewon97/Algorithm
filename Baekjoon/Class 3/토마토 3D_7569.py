import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
house = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
d = deque()
answer = 0
vis = [[[0] * m for _ in range(n)] for _ in range(h)]
dv = [0,0,0,0,-1,1]
dr = [-1,1,0,0,0,0]
dc = [0,0,-1,1,0,0]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if house[i][j][k] == 1:
                d.append((i, j, k, 0))
                vis[i][j][k] = 1

while d:
    v, r, c, days = d.popleft()

    if days > answer:
        answer = days

    for i in range(6):
        nv, nr, nc = v + dv[i], r + dr[i], c + dc[i]
        if 0 <= nv < h and 0 <= nr < n and 0 <= nc < m and not vis[nv][nr][nc] and house[nv][nr][nc] == 0:
            vis[nv][nr][nc] = 1
            house[nv][nr][nc] = 1
            d.append((nv, nr, nc, days+1))

has0 = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if house[i][j][k] == 0:
                has0 = True
                break
        if has0:
            break
    if has0:
        break

if has0:
    print(-1)
else:
    print(answer)