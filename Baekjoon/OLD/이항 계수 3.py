def power(a ,b):
    if b == 0:
        return 1
    if b % 2:
        return power(a, b // 2) ** 2 * a % mod
    else:
        return power(a, b // 2) ** 2 % mod


N, K = map(int, input().split())
mod = 1000000007

fact = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    fact[i] = fact[i-1] * i % mod

up = fact[N]
down = (fact[N - K] * fact[K]) % mod

print((up % mod) * (power(down, mod - 2) % mod) % mod)