import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stk = []
nums = deque(range(1, n+1))
arr = [int(input()) for _ in range(n)]
answer = []
can = True
for x in arr:
    while x not in stk:
        if not nums:
            can = False
            break
        stk.append(nums.popleft())
        answer.append('+')
    stk.pop()
    answer.append('-')

if can:
    print('\n'.join(answer))
else:
    print('NO')