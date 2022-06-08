from collections import deque

def scoreGap(a, r):
    score = [0, 0]
    for i in range(11):
        if a[i] == r[i] == 0:
            continue
        elif a[i] >= r[i]:
            score[0] += 10 - i
        else:
            score[1] += 10 - i
    return score[1] - score[0]


def bfs(n, info):
    res = []
    maxgap = 0
    d = deque()
    d.append((0, [0] * 11))
    
    while d:
        idx, arrow = d.popleft()
        
        if sum(arrow) == n:
            gap = scoreGap(info, arrow)
            if gap < maxgap:
                continue
            else:
                maxgap = gap
                res = arrow.copy()
                
        elif sum(arrow) > n:
            continue
        
        elif idx == 10:
            temp = arrow.copy()
            temp[idx] += n - sum(arrow)
            d.append((-1, temp))
        
        else:
            temp1 = arrow.copy()
            temp1[idx] += info[idx] + 1
            d.append((idx + 1, temp1))
            d.append((idx + 1, arrow))
    
    return [-1] if maxgap == 0 else res
    

def solution(n, info):
    answer = bfs(n, info)
    return answer if answer else [-1]