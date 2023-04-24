# https://school.programmers.co.kr/learn/courses/30/lessons/160585

def solution(board):
    win_list = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    board = ''.join(board)
    win_o = False
    win_x = False
    count_o = board.count("O")
    count_x = board.count("X")
    
    if count_o - count_x != 1 and count_o - count_x != 0:
        return 0
    
    for a,b,c in win_list:
        if board[a] == "O" and board[b] == "O" and board[c] == "O":
            win_o = True
            if count_o - count_x != 1:
                return 0
        if board[a] == "X" and board[b] == "X" and board[c] == "X":
            win_x = True
            if count_o - count_x != 0:
                return 0
            
    if win_o and win_x:
        return 0
    
    return 1