def backtracking(nqueens, row):
    return _backtracking_helper(nqueens, row)

def _backtracking_helper(nqueens, row):
    if row == nqueens.N:
        return True
    for col in range(nqueens.N):
        if nqueens.is_valid(row, col):
            nqueens.board.append(col)
            if _backtracking_helper(nqueens, row + 1):
                return True
            nqueens.board.pop()
    return False
