# 문자열 반복

t = int(input())

for _ in range(t):
    temp = input().split()
    r = int(temp[0])
    s = temp[1]

    for l in s:
        print(l * r, end='')

    print()