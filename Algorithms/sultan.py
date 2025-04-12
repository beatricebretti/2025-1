def solve(boards):
    def is_safe(row, col, cols, diag1, diag2):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

    def backtrack(row, current_sum, cols, diag1, diag2, board):
        nonlocal max_score
        if row == 8:
            max_score = max(max_score, current_sum)
            return
        for col in range(8):
            if is_safe(row, col, cols, diag1, diag2):
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                backtrack(row + 1, current_sum + board[row][col], cols, diag1, diag2, board)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
    results = []
    for board in boards:
        max_score = 0
        backtrack(0, 0, set(), set(), set(), board)
        results.append(max_score)
    return results

def read_input():
    k = int(input())
    boards = []
    for _ in range(k):
        board = []
        for _ in range(8):
            row = list(map(int, input().split()))
            board.append(row)
        boards.append(board)
    return boards

boards = read_input()
scores = solve(boards)
for score in scores:
    print(f"{score:5d}")