def brute_force(nqueens, row=0):
    return _brute_force_helper(nqueens, row)

def _brute_force_helper(nqueens, row):
    if row == nqueens.N:
        return True
    for col in range(nqueens.N):
        if nqueens.is_valid(row, col):
            nqueens.board.append(col)
            if _brute_force_helper(nqueens, row + 1):
                return True
            nqueens.board.pop()
    return False
