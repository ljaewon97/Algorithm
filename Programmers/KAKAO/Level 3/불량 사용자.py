from itertools import permutations
from collections import Counter

def chkWord(word, target):
    if len(word) != len(target):
        return False
    else:
        for i in range(len(word)):
            if target[i] != '*' and word[i] != target[i]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    lst = [i for i in range(len(user_id))]
    idxs_user_id = list(permutations(lst, len(banned_id)))
    
    for idx_user_id in idxs_user_id:
        for i in range(len(banned_id)):
            if not chkWord(user_id[idx_user_id[i]], banned_id[i]):
                break
        else:
            idx_user_id = set(idx_user_id)
            if idx_user_id not in answer:
                answer.append(idx_user_id)

    return len(answer)