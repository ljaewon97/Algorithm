def convertTime(time):
    time = time.split(':')
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])


def solution(play_time, adv_time, logs):
    play_time = convertTime(play_time)
    adv_time = convertTime(adv_time)
    dp = [0] * (play_time + 1)
    
    for log in logs:
        start, end = map(convertTime, log.split('-'))
        dp[start] += 1
        dp[end] -= 1
        
    for i in range(play_time):
        dp[i+1] += dp[i]
        
    default = 0
    s = 0
    for i in range(adv_time):
        default += dp[i]
        
    longest = default
    for i in range(play_time - adv_time):
        default = default - dp[i] + dp[i+adv_time]
        if default > longest:
            longest = default
            s = i + 1
    
    hour = s // 3600
    s -= hour * 3600
    minute = s // 60
    s -= minute * 60
    second = s
    
    return f'{hour:02}:{minute:02}:{second:02}'