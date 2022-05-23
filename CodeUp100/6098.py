maze = []

for _ in range(10):
    temp = list(map(int, input().split()))
    maze.append(temp)

r, c = 1, 1
while True:
    if maze[r][c] == 2:
        maze[r][c] = 9
        break
    elif r == 8 and c == 8:
        maze[r][c] = 9
        break
    maze[r][c] = 9
    if maze[r][c+1] == 1:
        r += 1
    else:
        c += 1

for i in range(10):
    for j in range(10):
        print(maze[i][j], end=' ')
    print()