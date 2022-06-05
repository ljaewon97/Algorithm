def checkBracket(a):
    stk = []
    for i in a:
        if i == '(':
            stk.append(i)
        else:
            if not stk:
                return False
            else:
                stk.pop()
    if stk:
        return False
    else:
        return True
    

def solution(p):
    if not p:
        return p
    
    u = ''
    while p:
        u += p[0]
        p = p[1:]
        if u.count('(') == u.count(')'):
            break
    v = p
    
    if checkBracket(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer