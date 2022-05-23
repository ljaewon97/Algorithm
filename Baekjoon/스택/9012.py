# 괄호

def checkBrackets(s):
    stk = []
    for l in s:
        if l == '(':
            stk.append(l)
        elif l == ')' and len(stk) == 0:
            return False
        elif l == ')' and stk[-1] == '(':
            stk.pop()

    if len(stk) == 0:
        return True
    else:
        return False


n = int(input())
for _ in range(n):
    s = input()
    res = checkBrackets(s)
    if res == True:
        print('YES')
    else:
        print('NO')