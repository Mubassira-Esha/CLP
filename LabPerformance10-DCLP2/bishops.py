def is_safe(board, row, col, N):
    for i in range(row):
        for j in range(N):
            if board[i][j] == 1:
                if abs(i - row) == abs(j - col):
                    return False
    return True

def place_bishops(board, row, N):
    if row == N:
        return True
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if place_bishops(board, row + 1, N):
                return True
            board[row][col] = 0
    return False

def print_board(board, N):
    for i in range(N):
        print(' '.join(map(str, board[i])))

def solve_bishops(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if place_bishops(board, 0, N):
        print_board(board, N)
    else:
        print("No solution found")

if __name__ == "__main__":
    N = int(input())
    solve_bishops(N)
