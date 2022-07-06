from itertools import permutations

for tc in range(1, int(input()) + 1):
    n, k = input().split()
    k = int(k)
    n = list(map(int, list(n)))
    n2 = sorted(n[:], reverse=True)
    a = []
    for i in range(len(n)):
        if n[i] == max(n):
            a.append(i)
    
    if n == n2 and len(a) > 1:
        print(f'#{tc} {int("".join(map(str, n)))}')
        continue
    
    for i in range(len(n)):
        m, idx = 0, 0
        for j in range(len(n)-1, i-1, -1):
            if n[j] > m:
                m = n[j]
                idx = j
        if i != idx:
            n[i], n[idx] = n[idx], n[i]
            k -= 1
        if k == 0:
            break

    if k and k % 2 == 1:
        n[-1], n[-2] = n[-2], n[-1]
    
    cand = []
    if len(a) > 1:
        for case in list(permutations(a, len(a))):
            temp = []
            j = 0
            for i in range(len(n)):
                if i in a:
                    temp.append(n[case[j]])
                    j += 1
                else:
                    temp.append(n[i])
            cand.append(int(''.join(map(str, temp))))
    
    
        print(f'#{tc} {max(cand)}')
    else:
        print(f'#{tc} {int("".join(map(str, n)))}')
        