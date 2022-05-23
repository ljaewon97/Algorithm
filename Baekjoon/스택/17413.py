# 단어 뒤집기 2

import sys

S = sys.stdin.readline()
stk = []
tag = False

for i in range(len(S)):
    if S[i] == '<':
        for j in list(reversed(stk)):
            print(j, end='')
        stk = []
        tag = True
        stk.append(S[i])
    elif S[i] == '>':
        stk.append(S[i])
        for j in stk:
            print(j, end='')
        stk = []
        tag = False
    elif (S[i] == ' ' or i == len(S) - 1) and tag == False:
        for j in list(reversed(stk)):
            print(j, end='')
        print(' ', end='')
        stk = []
    else:
        stk.append(S[i])