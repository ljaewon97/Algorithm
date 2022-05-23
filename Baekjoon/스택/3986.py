# 좋은 단어

def checkWord(s):
    stk = []
    for l in s:
        if stk and l == stk[-1]:
            stk.pop()
        else:
            stk.append(l)
    
    if stk:
        return False
    else:
        return True


n = int(input())
cnt = 0

for _ in range(n):
    s = input()
    if checkWord(s) == True:
        cnt += 1

print(cnt)