def solution(msg):
    answer = []
    d = {chr(i + 65) : (i + 1) for i in range(26)}
    
    while msg:
        for i in range(len(msg), 0, -1):
            x = msg[:i]
            if x in d:
                answer.append(d[x])
                d[msg[:i+1]] = list(d.values())[-1] + 1
                msg = msg[i:]
                break
    
    return answer