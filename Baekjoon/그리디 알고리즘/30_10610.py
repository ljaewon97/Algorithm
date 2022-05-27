import sys
input = sys.stdin.readline

n = input().rstrip()
n = sorted(n, reverse=True)

if '0' not in n:
    print(-1)
else:
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(n))