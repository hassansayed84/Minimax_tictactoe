"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    This will determine whos turn it is, player X goes first
    """
    x_count = sum(row.count(X) for row in board) #count x on board
    o_count = sum(row.count(O) for row in board) #count O on board
    return O if x_count > o_count else X #if there are more X's, O's turn, and vice versa

def actions(board):
    """
    Each action is represented as a tuple (i, j), 
    i corresponds to the row of the move (0, 1, or 2) and 
    j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2)
    possible action/move are only at an empty position on the board
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    """
    function takes a board and an action as input, and should return a new board state,
    without changing the original board
    """
    i, j = action
    if board[i][j] is not EMPTY: 
        raise Exception("Invalid move") #an action on a non empty move is prohibited
    new_board = [row[:] for row in board]  
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    checks for winner, winner must have 3 of  their moves in a row horizontally, vertically, or
    diagonally
    """

    # this checks for rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    # this checks for diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None #if no winner is found



def terminal(board):
    """
    accepts a board as input and return a boolean value indicating
    whether the game is over
    """
    if winner(board) is not None:
        return True #if there is a winner game is over
    for row in board:
        if EMPTY in row:
            return False #if all positions on the board are not filled, game is not over
    return True #this is if there is a tie, since all positions are filled but there is not winner



def utility(board):
    """
    Returns 1 if X won, -1 if O won, and 0 for a tie
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the most optimal move/action for AI
    if the board is at a terminal state function returns none
    """
    if terminal(board):
        return None

    if player(board) == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)
    return move

def max_value(board):
    """gets the maximum utility for X for the current board state"""
    if terminal(board):
        return utility(board), None
    v = float("-inf")
    move = None
    for action in actions(board):
        minValue = min_value(result(board, action))[0]
        if minValue > v:
            v, move = minValue, action
    return v, move

def min_value(board):
    """gets the minimum utiltiy for O for the current board state"""
    if terminal(board):
        return utility(board), None
    v = float("inf")
    move = None
    for action in actions(board):
        maxValue = max_value(result(board, action))[0]
        if maxValue < v:
            v, move = maxValue, action
    return v, move
