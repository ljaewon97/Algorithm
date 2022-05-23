# 막대기

n = int(input())
stick = []
m = 0
cnt = 0

for _ in range(n):
    stick.append(int(input()))

for i in range(len(stick)):
    if stick[-1] > m:
        m = stick[-1]
        cnt += 1
    stick.pop()

print(cnt)