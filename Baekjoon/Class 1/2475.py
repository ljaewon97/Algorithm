# 검증수

n = list(map(int, input().split()))
s = 0

for num in n:
    s += num ** 2

print(s % 10)