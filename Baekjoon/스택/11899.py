# 괄호 끼워넣기

s = input()
stk = []
cnt = 0

for l in s:
    if l == '(':
        stk.append(l)
    elif l == ')' and not stk:
        cnt += 1
    elif l == ')' and stk[-1] == '(':
        stk.pop()

cnt += len(stk)
print(cnt)