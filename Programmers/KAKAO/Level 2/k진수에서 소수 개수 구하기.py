def convert(n, k):
    res = ''
    while n > 0:
        res += str(n % k)
        n //= k
    return res[::-1]

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = convert(n, k)
    for i in num.split('0'):
        if i and isPrime(int(i)):
            answer += 1
    return answer