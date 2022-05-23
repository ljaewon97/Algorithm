from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
s = False

d = deque()
d.append([0, 0, board[0][0]])

while d and s == False:
    r, c, num = d.pop()
    visited[r][c] = 1

    for i in [0, num]:
        new_r = r + i
        new_c = c + num - i

        if new_r < n and new_c < n and visited[new_r][new_c] == 0:
            new_num = board[new_r][new_c]
            d.append([new_r, new_c, new_num])
            if new_num == -1:
                s = True

if s == False:
    print('Hing')
else:
    print('HaruHaru')