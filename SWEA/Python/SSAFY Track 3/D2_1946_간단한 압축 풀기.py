T = int(input())
for t in range(T):
    N = int(input())
    s = ''
    for _ in range(N):
        Ci, Ki = input().split()
        s += Ci * int(Ki)
    
    print(f'#{t+1}')
    for i in range(0, len(s), 10):
        print(s[i:min(i+10, len(s))])