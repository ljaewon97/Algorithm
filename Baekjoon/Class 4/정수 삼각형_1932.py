n = int(input())
tri = []
dp = []

for i in range(n):
    tri.append(list(map(int, input().split())))
    dp.append([0] * (i+1))

dp[0][0] = tri[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + tri[i][0]
    dp[i][-1] = dp[i-1][-1] + tri[i][-1]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[n-1]))