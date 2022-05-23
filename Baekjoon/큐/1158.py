# 요세푸스 문제

from collections import deque

n, k = map(int, input().split())
y = deque([i for i in range(1, n+1)])
ans = []

while y:
    for _ in range(k-1):
        y.append(y.popleft())
    ans.append(str(y.popleft()))

print('<' + ', '.join(ans[:]) + '>')