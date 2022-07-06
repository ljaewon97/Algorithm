for _ in range(int(input())):
    tc = int(input())
    cnt = [0] * 101
    nums = list(map(int, input().split()))
    for num in nums:
        cnt[num] += 1
    m, ans = 0, 0
    for i in range(100, -1, -1):
        if cnt[i] > m:
            m = cnt[i]
            ans = i
    print(f'#{tc} {ans}')