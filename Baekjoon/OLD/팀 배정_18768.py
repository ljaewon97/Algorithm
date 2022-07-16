import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))
    ad = []
    m = 0

    for i in range(n):
        ad.append([a[i], d[i]])
        if a[i] > d[i]:
            m += 1
        elif a[i] < d[i]:
            m -= 1
    
    first, second = 0, 1
    if m < 0:
        first, second = 1, 0
    
    ad = sorted(ad, key= lambda x : (x[first] - x[second], x[first]), reverse=True)
    idx_a = int(n / 2 + k / 2)
    idx_d = n - idx_a
    temp = idx_d
    attack, defence = 0, 0
    for i in range(idx_a):
        attack += ad[i][first]
    for i in range(n-1, n-idx_d-1, -1):
        defence += ad[i][second]
    abil = attack + defence
    
    while idx_a >= temp:
        if ad[idx_a-1][first] < ad[idx_a-1][second]:
            abil = abil + ad[idx_a-1][second] - ad[idx_a-1][first]
            idx_a -= 1
        else:
            break
    
    print(abil)