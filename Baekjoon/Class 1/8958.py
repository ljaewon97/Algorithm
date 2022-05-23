# OX퀴즈

t = int(input())

for _ in range(t):
    s = 0
    n = 0
    q = input()
    for i in q:
        if i == 'O':
            n += 1
            s += n
        elif i == 'X':
            n = 0

    print(s)