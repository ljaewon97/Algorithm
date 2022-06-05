def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = bin(arr1[i] | arr2[i])[2:]
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        if len(temp) < n:
            temp = ' ' * (n - len(temp)) + temp
        answer.append(temp)
    return answer