# 뱀

import sys
from collections import deque

direction = [[0,1], [1,0], [0,-1], [-1,0]]
d = 0
rotate = dict()
t_rot = []
snake = deque([[1,1]])
sec = 0

n = int(sys.stdin.readline()) + 2
board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(0, n, n-1):
    for j in range(1, n-1):
        board[i][j] = 2
        board[j][i] = 2

k = int(sys.stdin.readline())

for _ in range(k):
    i, j = map(int, sys.stdin.readline().split())
    board[i][j] = 1

l = int(sys.stdin.readline())

for _ in range(l):
    temp = sys.stdin.readline().split()
    rotate[int(temp[0])] = temp[1]
    t_rot.append(int(temp[0]))

while True:
    sec += 1
    next_r = snake[0][0] + direction[d][0]
    next_c = snake[0][1] + direction[d][1]

    if board[next_r][next_c] == 2 or [next_r, next_c] in snake:
        break

    snake.appendleft([next_r, next_c])
    if board[next_r][next_c] == 0:
        snake.pop()
    elif board[next_r][next_c] == 1:
        board[next_r][next_c] = 0

    if sec in t_rot:
        if rotate[sec] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

print(sec)