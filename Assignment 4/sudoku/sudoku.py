def check_valid(board, r, c, val):
    for i in range(9):
        if board[r][i] == val or board[i][c] == val:
            return False

    sr = r - r % 3
    sc = c - c % 3

    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if board[i][j] == val:
                return False

    return True


def sudoku_solver(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:

                for val in range(1, 10):
                    if check_valid(board, r, c, val):

                        board[r][c] = val

                        if sudoku_solver(board):
                            return True

                        board[r][c] = 0

                return False

    return True


def display(board):
    for row in board:
        print(row)


grid = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]

print("Original Sudoku:")
display(grid)

sudoku_solver(grid)

print("\nSolved Sudoku:")
display(grid)