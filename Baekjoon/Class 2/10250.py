# ACM 호텔

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        a = h
        b = n // h
    else:
        a = n % h
        b = n // h + 1
    ans = str(a)
    if b < 10:
        ans += '0' + str(b)
    else:
        ans += str(b)

    print(ans)