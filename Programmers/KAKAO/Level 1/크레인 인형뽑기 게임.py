def solution(board, moves):
    answer = 0
    stk = [[] for _ in range(len(board))]
    basket = []
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board)):
            if board[i][j] != 0:
                stk[j].append(board[i][j])
    
    for move in moves:
        if stk[move-1]:
            basket.append(stk[move-1].pop())
            if len(basket) > 1 and basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer