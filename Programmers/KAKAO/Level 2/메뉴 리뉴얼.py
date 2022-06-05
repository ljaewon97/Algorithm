def comb(arr, n):
    res = []
    if n > len(arr):
        return res
    
    if n == 1:
        for i in arr:
            res.append([i])
    else:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i+1:], n-1):
                res.append([arr[i]] + j)
    
    return res


def solution(orders, course):
    answer = []
    
    for n in course:
        cand = []
        d = dict()
        for order in orders:
            temp = comb(sorted(list(order)), n)
            for t in temp:
                cand.append(tuple(t))
        
        for c in cand:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        ma = max(list(d.values())) if d else 0
        if ma > 1:
            for key, value in d.items():
                if value == ma:
                    answer.append(''.join(key))
    
    return sorted(answer)