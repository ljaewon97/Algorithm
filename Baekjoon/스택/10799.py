# 쇠막대기

import sys

S = sys.stdin.readline()
stk = list()
prev = None
piece = 0

for l in S:
    if l == '(':
        stk.append(0)
    elif l == ')' and prev == '(':
        for i in range(len(stk)):
            stk[i] += 1
        stk.pop()
    elif l == ')':
        piece += stk.pop() + 1
    prev = l

print(piece)
