def solution(new_id):
    # step 1
    new_id = new_id.lower()
    new_id = list(new_id)

    # step 2
    temp = []
    for char in new_id:
        if char.isalpha() or char.isdecimal() or char in ['-', '_', '.']:
            temp.append(char)
    new_id = temp

    # step 3
    temp = [new_id[0]]
    for i in range(1, len(new_id)):
        if new_id[i-1] == new_id[i] == '.':
            continue
        else:
            temp.append(new_id[i])
    new_id = temp

    # step 4
    if new_id and new_id[0] == '.':
        new_id.pop(0)
    if new_id and new_id[-1] == '.':
        new_id.pop()

    # step 5
    if not new_id:
        new_id = ['a']

    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop()

    # step 7
    if len(new_id) <= 2:
        temp = new_id[-1]
        for _ in range(3 - len(new_id)):
            new_id.append(temp)

    answer = ''.join(new_id)

    return answer