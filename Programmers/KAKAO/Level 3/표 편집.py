def solution(n, k, cmds):
    class node:
        def __init__(self, idx, up, down):
            self.idx = idx
            self.up = up
            self.down = down
            self.state = 'O'
    
    table = []
    trash = []
    for i in range(n):
        table.append(node(i, i-1, i+1))
    table[0].up = None
    table[n-1].down = None
    
    for cmd in cmds:
        cmd = cmd.split()
        if cmd[0] == 'U':
            for _ in range(int(cmd[1])):
                k = table[k].up
        elif cmd[0] == 'D':
            for _ in range(int(cmd[1])):
                k = table[k].down
        elif cmd[0] == 'C':
            cur = table[k]
            cur.state = 'X'
            trash.append(cur)
            if cur.up != None:
                table[cur.up].down = cur.down
            if cur.down != None:
                table[cur.down].up = cur.up
            k = cur.down if cur.down != None else cur.up
        elif cmd[0] == 'Z':
            cur = trash.pop()
            cur.state = 'O'
            if cur.up != None:
                table[cur.up].down = cur.idx
            if cur.down != None:
                table[cur.down].up = cur.idx
    
    return ''.join([n.state for n in table])