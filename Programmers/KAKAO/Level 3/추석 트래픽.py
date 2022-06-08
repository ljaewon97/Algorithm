def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    
    for line in lines:
        line = line.split()
        time = line[1].split(':')
        end2milli = int(time[0]) * 60 * 60 * 1000 + int(time[1]) * 60 * 1000 + int(time[2].split('.')[0]) * 1000 + int(time[2].split('.')[1])
        process = line[2][:-1].split('.')
        if len(process) == 1:
            t_pro = int(process[0]) * 1000
        else:
            t_pro = int(process[0]) * 1000 + int(process[1]) * (10 ** (3 - len(process[1])))
        start2milli = end2milli - t_pro + 1
        
        start_time.append(start2milli)
        end_time.append(end2milli)
        
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
        
    return answer