from collections import defaultdict

def solution(gems):
    answer = []
    length = float('inf')
    gems_set = set(gems)
    d = defaultdict(int)
    right = 0
    
    for left, gem in enumerate(gems):
        while len(d) < len(gems_set) and right < len(gems):
            d[gems[right]] += 1
            right += 1
        
        if len(d) == len(gems_set):
            if right - left < length:
                length = right - left
                answer = [left + 1, right]
        
        d[gem] -= 1
        if d[gem] == 0:
            del d[gem] 
        
    return answer