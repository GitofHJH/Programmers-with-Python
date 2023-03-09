def solution(board, moves):
    N=len(board)
    answer = 0
    basket = []
    finddoll = False

    for x in moves:
        finddoll = False
        for y in range(N):
            if board[y][x-1] == 0 or finddoll == True:
                continue
            else:
                finddoll = True
                basket.append(board[y][x-1])
                if len(basket)>=2 and basket[-1] == basket[-2]:
                    answer += 2
                    del basket[-2:]
                board[y][x-1] = 0
                
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))