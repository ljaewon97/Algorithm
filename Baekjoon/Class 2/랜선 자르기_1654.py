import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]
left = 1
right = max(lans)
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid
    if cnt < n:
        right = mid - 1
    else:
        left = mid + 1

print(right)