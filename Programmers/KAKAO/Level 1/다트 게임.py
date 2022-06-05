def solution(dartResult):
    answer = []
    bonusDict = {'S':1, 'D':2, 'T':3}
    while dartResult:
        if dartResult.startswith('10'):
            score = int(dartResult[:2])
            bonus = dartResult[2]
            answer.append(score ** bonusDict[bonus])
            if len(dartResult) == 3:
                break
            else:
                dartResult = dartResult[3:]
        else:
            score = int(dartResult[:1])
            bonus = dartResult[1]
            answer.append(score ** bonusDict[bonus])
            if len(dartResult) == 2:
                break
            else:
                dartResult = dartResult[2:]

        if dartResult[0] == '*':
            if len(answer) == 1:
                answer[0] *= 2
            else:
                answer[-1] *= 2
                answer[-2] *= 2
            if len(dartResult) == 1:
                break
            else:
                dartResult = dartResult[1:]
        elif dartResult[0] == '#':
            answer[-1] *= -1
            if len(dartResult) == 1:
                break
            else:
                dartResult = dartResult[1:]

    return sum(answer)