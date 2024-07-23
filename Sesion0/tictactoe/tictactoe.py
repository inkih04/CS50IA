"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None




class NotValidAction(Exception):
    def __init__(self,mensaje="Not Valid Action"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f'{self.mensaje}'





def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def firstTurn(board):
    for raw in board:
        for col in raw:
            if col != EMPTY:
                return False
    return True

def isX_Turn(board):
    number_x = 0
    number_o = 0
    for raw in board:
        for col in raw:
            if col == X:
                number_x += 1
            elif col == O:
                number_o += 1           
    return number_x <= number_o



def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return EMPTY
    if firstTurn(board):
        return X
    if isX_Turn(board):
        return X
    else:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return EMPTY
    acts = set()
    print("Posible Actions -------------------")
    for i,raw in enumerate(board):
        for j,col in enumerate(raw):
            if col is EMPTY:
                print(f"col:{col} {col is EMPTY}")
                acts.add((i,j))

    print(acts)
    print("-----------------------------------------")
    return acts
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    newBoard = copy.deepcopy(board)
    try:
        if terminal(board):
            raise NotValidAction()
        elif (i < 0 or i >= len(board)) or (j < 0 or j >= len(board)):
            raise NotValidAction()
        elif board[i][j] != EMPTY:
            raise NotValidAction()
    except NotValidAction:
        print(f"Not Valid Action {i}{j}")
        exit(0)
    else:
        if X == player(board):
            newBoard[i][j] = X
        else:
            newBoard[i][j] = O
        return newBoard





def hWinner(board, i, j):
    if i == 0:
        return board[i][j] == board[i+1][j] == board[i+2][j]
    elif i == 1:
        return board[i-1][j] == board[i][j] == board[i+1][j]
    else:
        return board[i-2][j] == board[i-1][j] == board[i][j]

def vWInner(board, i, j):
    if j == 0:
        return board[i][j] == board[i][j+1] == board[i][j+2]
    elif j == 1:
        return board[i][j-1] == board[i][j] == board[i][j+1]
    else:
        return board[i][j-2] == board[i][j-1] == board[i][j]



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] !=EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    if board[0][0] != EMPTY and (hWinner(board, 0, 0) or vWInner(board, 0, 0)):
        return board[0][0]
    if board[1][1] != EMPTY and (hWinner(board, 1, 1) or vWInner(board, 1, 1)):
        return board[1][1]
    if board[2][2] != EMPTY and (hWinner(board, 2, 2) or vWInner(board, 2, 2)):
        return board[2][2]
    
    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == EMPTY:
        for raw in board:
            for col in raw:
                if col == EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0

def minValue(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
        if v == -1:
            return -1
    return v

        
def maxValue(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
        if v == 1:
            return 1
    return v






def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    bestAction = None

    if player(board) == X:
        bestScore = float('-inf')
        for action in actions(board):
            score = minValue(result(board, action))
            if score > bestScore:
                bestScore = score
                bestAction = action
    else:
        bestScore = float('inf')
        for action in actions(board):
            score = maxValue(result(board, action))
            if score < bestScore:
                bestScore = score
                bestAction = action

    return bestAction




