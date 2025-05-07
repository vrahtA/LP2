def solve_n_queens(n):
    board = [-1] * n  # board[i] is the column of the queen in row i
    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True
    def place_queens(row):
        if row == n:
            print_solution()
            return True  # Stop after first solution
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if place_queens(row + 1):
                    return True
        return False
    def print_solution():
        for i in range(n):
            row = ['.'] * n
            row[board[i]] = 'Q'
            print(''.join(row))
    place_queens(0)
solve_n_queens(7)
