def solution(m, musicinfos):
    answer = ''
    t = 0
    m2 = []
    for char in m:
        if char == '#':
            m2[-1] = m2[-1] + '#'
        else:
            m2.append(char)
    
    for music in musicinfos:
        music = music.split(',')
        start = int(music[0][:2]) * 60 + int(music[0][3:])
        end = int(music[1][:2]) * 60 + int(music[1][3:])
        time = end - start
        title = music[2]
        played = []
        for char in music[3]:
            if char == '#':
                played[-1] = played[-1] + '#'
            else:
                played.append(char)
        
        repeated = []
        for i in range(time):
            repeated.append(played[i % len(played)])           
        
        for i in range(len(repeated) - len(m2) + 1):
            con = True
            for j in range(len(m2)):
                if m2[j] != repeated[i+j]:
                    con = False
            if con:
                if time > t:
                    answer = title
                    t = time
                    break
    
    if t == 0:
        return '(None)'
    else:     
        return answer