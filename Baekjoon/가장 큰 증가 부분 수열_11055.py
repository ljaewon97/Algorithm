import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = [0] * n
s[0] = arr[0]

for i in range(1, n):
    ma = 0
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i] and s[j] > ma:
            ma = s[j]
    s[i] = ma + arr[i]

print(max(s))