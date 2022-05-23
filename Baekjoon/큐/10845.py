# 큐

from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    temp = sys.stdin.readline().split()
    if temp[0] == 'push':
        queue.append(int(temp[1]))
    elif temp[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif temp[0] == 'size':
        print(len(queue))
    elif temp[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif temp[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif temp[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])