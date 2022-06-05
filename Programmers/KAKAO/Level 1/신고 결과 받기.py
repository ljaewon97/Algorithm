def solution(id_list, report, k):
    reportDict = {name : set() for name in id_list}
    answerDict = {name : 0 for name in id_list}
        
    for rep in report:
        a, b = rep.split()
        reportDict[b].add(a)
        
    for id in id_list:
        if len(reportDict[id]) >= k:
            for x in reportDict[id]:
                answerDict[x] += 1
    
    answer = list(answerDict.values())
        
    return answer