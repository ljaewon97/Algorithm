from collections import deque

def search(sr, sc, size):
    fishes = []
    d = deque()
    d.append((sr, sc, 0))
    v = [[0] * n for _ in range(n)]
    v[sr][sc] = 1

    while d:
        r, c, dist = d.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not v[nr][nc] and space[nr][nc] <= size:
                if 0 < space[nr][nc] < size:
                    fishes.append((dist+1, nr, nc))
                v[nr][nc] = 1
                d.append((nr, nc, dist+1))

    return fishes


n = int(input())
size = 2
sizeup = 0
time = 0
space = [list(map(int, input().split())) for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            r = i
            c = j

while True:
    fishes = search(r, c, size)
    fishes.sort()

    if not fishes:
        print(time)
        break
    
    space[r][c] = 0
    r, c = fishes[0][1], fishes[0][2]
    time += fishes[0][0]
    sizeup += 1
    if sizeup == size:
        size += 1
        sizeup = 0