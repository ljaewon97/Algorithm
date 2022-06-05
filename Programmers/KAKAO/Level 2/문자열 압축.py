def zipString(s, n):
    res = ''
    arr = []
    for i in range(0, len(s), n):
        arr.append(s[i:min(i+n, len(s))])
    
    cur = ''
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != cur:
            cur = arr[i]
            cnt = 1
        else:
            cnt += 1
        
        if i == len(arr) -1 or arr[i] != arr[i+1]:
            if cnt >= 2:
                res += str(cnt) + cur
            else:
                res += cur
    
    return len(res)


def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        temp = zipString(s, i)
        if temp < answer:
            answer = temp
    return answer