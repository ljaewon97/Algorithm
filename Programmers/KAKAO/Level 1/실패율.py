def solution(N, stages):
    failratio = []
    user = len(stages)
    for i in range(1, N+1):
        a = stages.count(i)
        try:
            failratio.append([a / user, i])
        except:
            failratio.append([0, i])
        user -= a
        
    failratio = sorted(failratio, key = lambda x : -x[0])
    answer = [x[1] for x in failratio]
    
    return answer