def isPalindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-(i+1)]:
            return False
    return True

T = int(input())
for i in range(T):
    word = input()
    ans = 0
    if isPalindrome(word):
        ans = 1
    print(f'#{i+1} {ans}')