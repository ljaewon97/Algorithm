while True:
    str = input()
    if str == '.':
        break

    arr = []
    for s in str:
        if s in ['(', ')', '[', ']']:
            arr.append(s)
    
    valid = True
    stk = []
    chk = {')':'(', ']':'['}
    for b in arr:
        if b in ['(', '[']:
            stk.append(b)
        else:
            if not stk:
                valid = False
            else:
                temp = stk.pop()
                if chk[b] != temp:
                    valid = False
    
    if stk:
        valid = False

    print('yes' if valid else 'no')