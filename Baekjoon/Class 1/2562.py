# 최댓값

m = 0
idx = 0

for i in range(1, 10):
    n = int(input())
    if n > m:
        m = n
        idx = i

print(m)
print(idx)