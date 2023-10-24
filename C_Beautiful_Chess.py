t = int(input())

for _ in range(t):
    input()    
    board = []
    for _ in range(8):
        board.append(input())
    
    for row in range(1, 7):
        for col in range(1, 7):
            if board[row-1][col-1] == '#' and board[row-1][col+1] == '#' and board[row+1][col-1] == '#' and board[row+1][col+1] == '#':
                print(str(row + 1) +" "+ str(col + 1))
