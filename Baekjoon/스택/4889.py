# 안정적인 문자열

import sys

s = sys.stdin.readline()
i = 0

while(s[0] != '-'):
    stk = []
    cnt = 0
    for l in s:
        if l == '{':
            stk.append(l)
        elif l == '}' and len(stk) == 0:
            cnt += 1
            stk.append('{')
        elif l == '}' and stk[-1] == '{':
            stk.pop()
    cnt += len(stk) // 2
    
    print(f'{i+1}. {cnt}')
    i += 1
    s = sys.stdin.readline()