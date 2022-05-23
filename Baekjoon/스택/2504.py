# 괄호의 값

import sys

def calcBracket(S):
    stk = []

    for l in S:
        if l == '(' or l == '[':
            stk.append(l)
        elif l == ')':
            if stk[-1] == '(':
                stk[-1] = 2
            else:
                temp = 0
                for i in range(len(stk)-1, -1, -1):
                    if stk[i] == '(':
                        stk[-1] = 2 * temp
                        break
                    else:
                        temp += stk[i]
                        stk = stk[:-1]
        elif l == ']':
            if stk[-1] == '[':
                stk[-1] = 3
            else:
                temp = 0
                for i in range(len(stk)-1, -1, -1):
                    if stk[i] == '[':
                        stk[-1] = 3 * temp
                        break
                    else:
                        temp += stk[i]
                        stk = stk[:-1]

    return sum(stk)


def checkBracket(S):
    stk = []

    for l in S:
        if l == '(' or l == '[':
            stk.append(l)
        elif (l == ')' or l == ']') and len(stk) == 0:
            return 0
        elif l == ')' and stk[-1] == '(':
            stk.pop()
        elif l == ']' and stk[-1] == '[':
            stk.pop()

    if len(stk) == 0:
        return 1
    else:
        return 0
        

S = sys.stdin.readline()

valid = checkBracket(S)

if valid:
    print(calcBracket(S))
else:
    print(0)