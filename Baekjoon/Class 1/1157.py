# 단어 공부

w = input()
al = [0 for _ in range(26)]

for l in w:
    if l.isupper():
        al[ord(l) - ord('A')] += 1
    elif l.islower():
        al[ord(l) - ord('a')] += 1

if al.count(max(al)) > 1:
    print('?')
else:
    print(chr(ord('A') + al.index(max(al))))