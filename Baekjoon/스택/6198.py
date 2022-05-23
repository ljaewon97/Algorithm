# 옥상 정원 꾸미기

import sys

n = int(sys.stdin.readline())
h = [int(sys.stdin.readline()) for _ in range(n)]
stk = []
ans = 0

for i in range(n):
    while stk and h[i] >= stk[-1]:
            stk.pop()
    stk.append(h[i])
    ans += len(stk) - 1
    
print(ans)