from itertools import combinations

def solution(relation):
    answer = 0
    table = [[] for _ in range(len(relation[0]))]
    for r in relation:
        for i in range(len(r)):
            table[i].append(r[i])
    
    cols = [i for i in range(len(table))]
    uni = []

    for i in range(1, len(table)+1):
        combs = combinations(cols, i)
        for comb in combs:
            arr = []
            for j in range(len(relation)):
                temp = []
                for c in comb:
                    temp.append(table[c][j])
                arr.append(tuple(temp))
            if len(arr) == len(set(arr)):
                uni.append(comb)
                
    while uni:
        cur = set(uni.pop(0))
        answer += 1
        erase = []
        for comb in uni:
            if cur.issubset(set(comb)):
                erase.append(comb)
        for comb in erase:
            uni.remove(comb)

    return answer