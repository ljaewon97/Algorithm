from itertools import permutations
import copy

def calc(lst, prior):
    for p in prior:
        while p in lst:
            idx = lst.index(p) - 1
            a = lst.pop(idx)
            op = lst.pop(idx)
            b = lst.pop(idx)
            if op == '+':
                temp = a + b
            elif op == '-':
                temp = a - b
            else:
                temp = a * b
            lst.insert(idx, temp)
    return abs(lst[0])
        

def solution(expression):
    answer = 0
    ex = []
    oper = set()
    temp = ''
    for char in expression:
        if char.isdigit():
            temp += char
        else:
            ex.append(int(temp))
            temp = ''
            ex.append(char)
            oper.add(char)
    ex.append(int(temp))
    priority = list(permutations(oper, len(oper)))
    
    for prior in priority:
        lst = copy.deepcopy(ex)
        temp = calc(lst, prior)
        if temp > answer:
            answer = temp
    
    return answer