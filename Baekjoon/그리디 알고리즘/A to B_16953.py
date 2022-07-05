from collections import deque

a, b = map(int, input().split())
d = deque()
d.append((a, 1))
answer = -1

while d:
    cur, step = d.popleft()
    if cur == b:
        answer = step
        break
    n1 = cur * 10 + 1
    n2 = cur * 2
    if n1 <= b:
        d.append((n1, step+1))
    if n2 <= b:
        d.append((n2, step+1))
    
print(answer)