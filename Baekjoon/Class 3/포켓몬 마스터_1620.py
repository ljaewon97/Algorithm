import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = dict()

for i in range(n):
    name = input().strip()
    p[name] = str(i+1)
    p[str(i+1)] = name

for i in range(m):
    print(p[input().strip()])