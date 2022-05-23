# 덱

from collections import deque
import sys

n = int(sys.stdin.readline())
d = deque()

for _ in range(n):
    temp = sys.stdin.readline().split()
    if temp[0] == 'push_front':
        d.appendleft(int(temp[1]))
    elif temp[0] == 'push_back':
        d.append(int(temp[1]))
    elif temp[0] == 'pop_front':
        if not d:
            print(-1)
        else:
            print(d.popleft())
    elif temp[0] == 'pop_back':
        if not d:
            print(-1)
        else:
            print(d.pop())
    elif temp[0] == 'size':
        print(len(d))
    elif temp[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif temp[0] == 'front':
        if not d:
            print(-1)
        else:
            print(d[0])
    elif temp[0] == 'back':
        if not d:
            print(-1)
        else:
            print(d[-1])