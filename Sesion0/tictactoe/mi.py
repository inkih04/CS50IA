X = "X"
O = "O"
EMPTY = None

def minValue(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
        if v == -1:
            return -1
    return v
        
def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
        if v == 1:
            return 1
    return v





def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    puntuacionMin = 2
    puntuacionMax = -2
    #a ->0 empate a->-1 gana O a->1 gana X

    if terminal(board):
        return None
    bestAction = None

    for action in actions(board):
        if player(board) == X:
            newValue = maxValue(board)
            if puntuacionMax < newValue:
                puntuacionMax = newValue
                bestAction = action
        else:
            newValue = minValue(board)
            if puntuacionMin < newValue:
                puntuacionMin = newValue
                bestAction = action


def main():
    board = [[X, X, X],
            [EMPTY, 0, X],
            [O, X, X]]
    print(board)
    print(hWInner(board, 0, 0))
    
if __name__ == "__main__":
    main()