# 후위 표기식2

n = int(input())
s = input()
o = ['*', '+', '/', '-']
stk = []
num = []

for _ in range(n):
    num.append(int(input()))

for i in s:
    if i not in o:
        stk.append(num[ord(i) - 65])
    elif i == '+':
        b = stk.pop()
        c = stk.pop()
        stk.append(c + b)
    elif i == '-':
        b = stk.pop()
        c = stk.pop()
        stk.append(c - b)
    elif i == '*':
        b = stk.pop()
        c = stk.pop()
        stk.append(c * b)
    elif i == '/':
        b = stk.pop()
        c = stk.pop()
        stk.append(c / b)

print(format(stk[0], '.2f'))