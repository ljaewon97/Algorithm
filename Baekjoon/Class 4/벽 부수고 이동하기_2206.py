from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global n, m, maze
    d = deque()
    d.append((0, 0, 1, 1))
    v = [[0] * m for _ in range(n)]
    vc = [[0] * m for _ in range(n)]
    v[0][0] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while d:
        r, c, dist, crack = d.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr == n - 1 and nc == m - 1:
                return dist + 1
            elif 0 <= nr < n and 0 <= nc < m and crack and maze[nr][nc] == '0' and not v[nr][nc]:
                v[nr][nc] = 1
                d.append((nr, nc, dist+1, crack))
            elif 0 <= nr < n and 0 <= nc < m and not crack and maze[nr][nc] == '0' and not vc[nr][nc]:
                vc[nr][nc] = 1
                d.append((nr, nc, dist+1, crack))
            elif 0 <= nr < n and 0 <= nc < m and crack and maze[nr][nc] == '1' and not v[nr][nc]:
                v[nr][nc] = 1
                d.append((nr, nc, dist+1, 0))

    return -1


n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(input())
print(1 if n == m == 1 else bfs())