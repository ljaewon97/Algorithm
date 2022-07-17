import sys
input = sys.stdin.readline

def dust():
    locs = []
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                locs.append((i, j, room[i][j]))
    
    while locs:
        r, c, amount = locs.pop()
        dirs = 0
        moved = int(amount / 5)

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                dirs += 1
                room[nr][nc] += moved
        
        room[r][c] -= dirs * moved


def cleaner(loc):
    up, down = loc, loc+1
    # Upper part
    for r in range(up-1, 0, -1):
        room[r][0] = room[r-1][0]
    for c in range(C-1):
        room[0][c] = room[0][c+1]
    for r in range(up):
        room[r][C-1] = room[r+1][C-1]
    for c in range(C-1, 1, -1):
        room[up][c] = room[up][c-1]
    room[up][1] = 0
    
    # Lower part
    for r in range(down+1, R-1):
        room[r][0] = room[r+1][0]
    for c in range(C-1):
        room[R-1][c] = room[R-1][c+1]
    for r in range(R-1, down, -1):
        room[r][C-1] = room[r-1][C-1]
    for c in range(C-1, 1, -1):
        room[down][c] = room[down][c-1]
    room[down][1] = 0


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
dr, dc = [-1,1,0,0], [0,0,-1,1]
answer = 0

for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            loc = i - 1
            
for _ in range(T):
    dust()
    cleaner(loc)

for i in range(R):
    answer += sum(room[i])

print(answer + 2)