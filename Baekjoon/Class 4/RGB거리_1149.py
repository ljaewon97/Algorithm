import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
dp = [rgb[0][0], rgb[0][1], rgb[0][2]]

for i in range(1, n):
    temp1 = dp[0]
    temp2 = dp[1]
    temp3 = dp[2]

    for j in range(3):
        if j == 0:
            dp[0] = temp2 + rgb[i][j] if temp2 < temp3 else temp3 + rgb[i][j]
        elif j == 1:
            dp[1] = temp1 + rgb[i][j] if temp1 < temp3 else temp3 + rgb[i][j]
        else:
            dp[2] = temp1 + rgb[i][j] if temp1 < temp2 else temp2 + rgb[i][j]

print(min(dp))