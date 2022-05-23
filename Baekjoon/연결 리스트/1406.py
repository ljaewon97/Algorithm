# 에디터

stk1 = list(input())
stk2 = []
m = int(input())


for _ in range(m):
    temp = input()
    if temp[0] == 'L':
        if stk1:
            stk2.append(stk1.pop())
    elif temp[0] == 'D':
        if stk2:
            stk1.append(stk2.pop())
    elif temp[0] == 'B':
        if stk1:
            stk1.pop()
    elif temp[0] == 'P':
        stk1.append(temp[2])

print(''.join(stk1 + list(reversed(stk2))))