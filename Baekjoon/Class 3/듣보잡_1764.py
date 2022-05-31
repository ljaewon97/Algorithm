import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(input().strip() for _ in range(n))
b = set(input().strip() for _ in range(m))
c = set()

if n > m:
    for i in b:
        if i in a:
            c.add(i)
else:
    for i in a:
        if i in b:
            c.add(i)

c = list(c)
c.sort()
print(len(c))
print('\n'.join(c))