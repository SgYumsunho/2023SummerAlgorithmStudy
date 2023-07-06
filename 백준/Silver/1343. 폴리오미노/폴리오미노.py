def solve_board(board)  :
    board = board.replace("XXXX", "AAAA")
    board = board.replace("XX", "BB")
    if board.count("X") != 0 :
        return -1
    else :
        return board

board = input()

result = solve_board(board)
print(result)
