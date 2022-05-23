# 프린터 큐

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    d = deque(map(int, sys.stdin.readline().split()))
    d2 = deque([1 for _ in range(n)])
    d2[m] = 2
    cnt = 0

    while True:
        if d[0] == max(d):
            d.popleft()
            cnt += 1
            if d2.popleft() == 2:
                break
        else:
            d.append(d.popleft())
            d2.append(d2.popleft())

    print(cnt)
