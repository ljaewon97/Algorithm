def jacade(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    set3 = set(lst1 + lst2)
    i, u = 0, 0
    
    for s in set3:
        if s in set1 and s in set2:
            i += min(lst1.count(s), lst2.count(s))
            u += max(lst1.count(s), lst2.count(s))
        else:
            u += max(lst1.count(s), lst2.count(s))
    
    sim = i / u if u != 0 else 1
    return int(sim * 65536)


def makeList(s):
    res = []
    for i in range(len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            res.append(s[i:i+2])
    return res


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    lst1 = makeList(str1)
    lst2 = makeList(str2)
    answer = jacade(lst1, lst2)
    
    return answer