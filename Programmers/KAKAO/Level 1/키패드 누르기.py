def solution(numbers, hand):
    answer = ''
    l, r = (3,0), (3,2)
    num_loc = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            l = num_loc[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            r = num_loc[num]
        else:
            dl = abs(l[0] - num_loc[num][0]) + abs(l[1] - num_loc[num][1])
            dr = abs(r[0] - num_loc[num][0]) + abs(r[1] - num_loc[num][1])
            if dl < dr or (dl == dr and hand == 'left'):
                answer += 'L'
                l = num_loc[num]
            else:
                answer += 'R'
                r = num_loc[num]
    
    return answer