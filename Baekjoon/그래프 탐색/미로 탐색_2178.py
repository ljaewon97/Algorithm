import sys
input = sys.stdin.readline
from collections import deque

def bfs(r, c):
    cnt = 1
    di = [-1,0,1,0]
    dj = [0,-1,0,1]
    d = deque()
    d.append([r, c, cnt])
    maze[r][c] = 0

    while d:
        i, j, k = d.popleft()
        for p in range(4):
            ni, nj = i + di[p], j + dj[p]
            if 0 <= ni < n and 0 <= nj < m:
                if ni == n - 1 and nj == m - 1:
                    ans.append(k+1)
                if maze[ni][nj] == '1':
                    maze[ni][nj] = 0
                    d.append([ni, nj, k+1])
    

n, m = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(n)]
ans = []

bfs(0, 0)
print(min(ans))