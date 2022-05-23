# 후위 표기식

s = input()
stk = []
res = ''

for l in s:
    if l.isalpha():
        res += l
    else:
        if l == '(':
            stk.append(l)
        elif l == '*' or l == '/':
            while stk and (stk[-1] == '*' or stk[-1] == '/'):
                res += stk.pop()
            stk.append(l)
        elif l == '+' or l == '-':
            while stk and stk[-1] != '(':
                res += stk.pop()
            stk.append(l)
        elif l == ')':
            while stk and stk[-1] != '(':
                res += stk.pop()
            stk.pop()

while stk:
    res += stk.pop()

print(res)