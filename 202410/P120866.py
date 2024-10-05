def solution(board):
    xi = [1,-1, 0, 0, 1,-1, 1, -1]
    xj = [0, 0, 1, -1, 1, -1, -1, 1]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] == 1:
                for x in range(8):
                    newj = j+xj[x]
                    newi = i+xi[x]
                    if 0<=newj<len(board) and 0<=newi<len(board):
                        if board[newj][newi] == 0:
                            board[newj][newi] = -1
    answer = 0
    for i in board:
        answer += i.count(0)
    return answer