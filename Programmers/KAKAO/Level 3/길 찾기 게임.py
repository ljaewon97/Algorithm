from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    num2x = {i+1 : nodeinfo[i][0] for i in range(len(nodeinfo))}
    x2num = {nodeinfo[i][0] : i+1 for i in range(len(nodeinfo))}
    y_cords = set()
    nodelevel = defaultdict(list)
    nodes = [[0] * 2 for _ in range(len(nodeinfo)+1)]
    
    for info in nodeinfo:
        y_cords.add(info[1])
        nodelevel[info[1]].append(info[0])
    y_cords = sorted(list(y_cords), reverse=True)
    
    def maketree(num, depth, ll, rl):
        if depth == len(y_cords):
            return
        
        x = num2x[num]
        for node in nodelevel[y_cords[depth]]:
            if ll <= node <= x:
                nodes[num][0] = x2num[node]
                maketree(x2num[node], depth+1, ll, x)
            elif x <= node <= rl:
                nodes[num][1] = x2num[node]
                maketree(x2num[node], depth+1, x, rl)
    
    root = x2num[nodelevel[y_cords[0]][0]]
    maketree(root, 1, 0, max(nodeinfo)[0])
    
    def preorder(n):
        if n == 0:
            return
        pre.append(n)
        preorder(nodes[n][0])
        preorder(nodes[n][1])
        
    def postorder(n):
        if n == 0:
            return
        postorder(nodes[n][0])
        postorder(nodes[n][1])
        post.append(n)
    
    pre = []
    post = []
    preorder(root)
    postorder(root)
    
    return [pre, post]