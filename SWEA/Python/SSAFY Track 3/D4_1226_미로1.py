from collections import deque

def bfs(maze, start):
    con = False
    dr, dc = [-1,1,0,0], [0,0,-1,1]
    d = deque()
    d.append(start)
    visited = [[0] * 16 for _ in range(16)]
    visited[start[0]][start[1]] = 1

    while d:
        r, c = d.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if maze[nr][nc] == 3:
                con = True
            elif maze[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = 1
                d.append((nr, nc))
        
        if con:
            break
    
    return 1 if con else 0


for _ in range(10):
    t = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = (i, j)
            
    ans = bfs(maze, start)
    print(f'#{t} {ans}')