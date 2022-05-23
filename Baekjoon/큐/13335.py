# 트럭

import sys
from collections import deque

n, w, l = map(int, sys.stdin.readline().split())
a = deque(map(int, sys.stdin.readline().split()))
b = deque([0 for _ in range(w)])
sec = 0

while True:
    if len(a) == 0 and sum(b) == 0:
        break
    
    if a:
        temp = a[0]
        b.popleft()
        if sum(b) + temp > l:
            b.append(0)
        else:
            b.append(a.popleft())
    else:
        b.popleft()
        b.append(0)
      
    sec += 1

print(sec)