import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
cnt = [[i, 0] if i <= 4000 else [i-8001, 0] for i in range(8001)]
for i in arr:
    cnt[i][1] += 1
cnt.sort(key=lambda x : (-x[1], x[0]))

print(int(round(sum(arr) / n)))
print(arr[n//2])
print(cnt[1][0] if cnt[0][1] == cnt[1][1] else cnt[0][0])
print(arr[-1] - arr[0])