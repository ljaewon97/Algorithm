# 스택

import sys

N = int(sys.stdin.readline())
stk = []

for _ in range(N):
    temp = sys.stdin.readline().split()
    if temp[0] == 'push':
        stk.append(int(temp[1]))
    elif temp[0] == 'pop':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif temp[0] == 'size':
        print(len(stk))
    elif temp[0] == 'empty':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif temp[0] == 'top':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])