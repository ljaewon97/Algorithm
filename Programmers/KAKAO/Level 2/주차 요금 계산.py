import math

def solution(fees, records):
    answer = []
    d = dict()
    for record in records:
        record = record.split()
        if record[1] not in d:
            d[record[1]] = []
        x = int(record[0][:2]) * 60 + int(record[0][3:])
        if record[2] == 'IN':
            x *= -1
        d[record[1]].append(x)
    
    for k in d.keys():
        if d[k][-1] <= 0:
            d[k].append(1439)
            
    d = dict(sorted(d.items()))
    for k in d.keys():
        m = sum(d[k])
        if m <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1]
            fee += math.ceil((m - fees[0]) / fees[2]) * fees[3]
            answer.append(fee)
    
    return answer