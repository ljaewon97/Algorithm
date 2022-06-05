def solution(record):
    answer = []
    logs = []
    userInfo = dict()
    
    for command in record:
        command = command.split()
        if command[0] == 'Enter':
            userID = command[1]
            userNick = command[2]
            userInfo[userID] = userNick
            logs.append([userID, 'in'])
        elif command[0] == 'Leave':
            userID = command[1]
            logs.append([userID, 'out'])
        else:
            userID = command[1]
            userNick = command[2]
            userInfo[userID] = userNick
    
    for log in logs:
        if log[1] == 'in':
            answer.append(userInfo[log[0]] + '님이 들어왔습니다.')
        else:
            answer.append(userInfo[log[0]] + '님이 나갔습니다.')
    
    return answer