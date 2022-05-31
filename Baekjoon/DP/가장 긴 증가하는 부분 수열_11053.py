import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = [0] * n
s[0] = 1

for i in range(1, n):
    m = 0
    for j in range(i-1, -1, -1):
        if a[j] < a[i] and s[j] > m:
            m = s[j]
    s[i] = m + 1

print(max(s))