def solution(n, r, c):
    global ans
    if n == 0:
        return
    if 0 <= r < 2 ** (n-1):
        if 0 <= c < 2 ** (n-1):
            temp = 0
        else:
            c -= 2 ** (n-1)
            temp = 1
    else:
        if 0 <= c < 2 ** (n-1):
            r -= 2 ** (n-1)
            temp = 2
        else:
            r -= 2 ** (n-1)
            c -= 2 ** (n-1)
            temp = 3
    
    ans += (4 ** (n-1)) * temp
    solution(n-1, r, c)
    

ans = 0
n, r, c = map(int, input().split())
solution(n, r, c)
print(ans)