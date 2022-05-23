# 평균

from statistics import mean

n = int(input())
score = list(map(int, input().split()))

a = mean(score)
m = max(score)

print(a / m * 100)