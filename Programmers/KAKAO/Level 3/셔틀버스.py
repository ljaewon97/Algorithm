from collections import deque

def min1earlier(time):
    time = time.split(':')
    hour = int(time[0])
    minute = int(time[1])
    m = hour * 60 + minute - 1
    hour = m // 60
    minute = m - (m // 60) * 60
    return f'{hour:02}:{minute:02}'


def solution(n, t, m, timetable):
    answer = ''
    timetable = deque(sorted(timetable))
    buses = []
    mi = 540
    for _ in range(n):
        hour = mi // 60
        minute = mi - (mi // 60) * 60
        buses.append(f'{hour:02}:{minute:02}')
        mi += t
    buses = deque(buses)
    
    while buses:
        cur_bus = buses.popleft()
        
        for i in range(m):
            if not buses and i == m - 1:
                if timetable:
                    if timetable[0] <= cur_bus:
                        return min1earlier(timetable[0])
                    else:
                        return cur_bus
                else:
                    return cur_bus
            if timetable and timetable[0] <= cur_bus:
                timetable.popleft()
    
    return answer