from collections import deque

n = int(input())
area = [list(input()) for _ in range(n)]
cnt = 0
ans = []

def bfs(r, c):
    cnt2 = 0
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]
    d = deque()
    d.append([r, c])
    area[r][c] = '0'

    while d:
        r, c = d.popleft()
        cnt2 += 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if area[nr][nc] == '1':
                    area[nr][nc] = '0'
                    d.append([nr, nc])
    
    ans.append(cnt2)

for i in range(n):
    for j in range(n):
        if area[i][j] == '1':
            bfs(i, j)
            cnt += 1

print(cnt)
ans.sort()
for i in range(len(ans)):
    print(ans[i])