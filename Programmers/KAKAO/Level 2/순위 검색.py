from bisect import bisect_left

def solution(info, query):
    answer = []
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), [])
                    
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))
    
    for d in data:
        data[d].sort()
        
    for q in query:
        q = q.split()
        i = (q[0], q[2], q[4], q[6])
        answer.append(len(data[i]) - bisect_left(data[i], int(q[7])))
        
    return answer