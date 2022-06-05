def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    d = {num : str(i) for i, num in enumerate(arr)}
    for i in arr:
        s = s.replace(i, d[i])
    return int(s)