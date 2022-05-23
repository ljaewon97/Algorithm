# 피보나치 함수

t = int(input())

for _ in range(t):
    n = int(input())
    f = [0, 1]

    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        for _ in range(n-1):
            f.append(f[-1]+f[-2])

        print(f[n-1], f[n])