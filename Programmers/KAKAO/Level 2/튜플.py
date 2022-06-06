def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    lst = []
    for i in s:
        lst.append(list(map(int, i.split(','))))
    lst.sort(key = lambda x : len(x))
    answer.append(lst[0][0])
    for i in range(len(lst)-1):
        answer += list(set(lst[i+1]) - set(lst[i]))
    return answer