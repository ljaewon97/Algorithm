import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
line.sort()
waiting = 0
ans = 0
for time in line:
    ans += waiting + time
    waiting += time
print(ans)