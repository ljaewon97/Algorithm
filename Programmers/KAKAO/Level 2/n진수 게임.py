def convert(num, n):
    if num == 0:
        return '0'
    d = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    res = ''
    while num > 0:
        x = num % n
        res += str(x) if x < 10 else d[x]
        num //= n
    return res[::-1]
    

def solution(n, t, m, p):
    answer = ''
    num = 0
    while len(answer) < (t * m):
        answer += convert(num, n)
        num += 1
    
    ans = ''
    for i in range(t * m):
        if i % m == p - 1:
            ans += answer[i]
        
    return ans