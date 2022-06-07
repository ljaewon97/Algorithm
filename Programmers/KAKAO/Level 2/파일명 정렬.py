def solution(files):
    out = []
    idx = 0
    
    for file in files:
        isFirst = True
        idx2 = len(file)
        for i in range(len(file)):
            if isFirst and file[i].isdigit():
                idx1 = i
                isFirst = False
            elif not isFirst and not file[i].isdigit():
                idx2 = i
                break
        
        head = file[:idx1].lower()
        num = int(file[idx1:idx2])
        tail = idx
        idx += 1
        out.append((file, head, num, tail))
        
    out.sort(key = lambda x : (x[1], x[2], x[3]))
    answer = [i[0] for i in out]
    
    return answer

print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))