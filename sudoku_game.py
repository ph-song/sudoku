"""
Template for Programming Assignment FIT1045 - S2 2021
Sudoku

Version 2 (2021-08-13)

Sudoku boards partially retrieved from
- https://puzzlemadness.co.uk
- https://sudokudragon.com
"""

########### Sudoku boards ##############################

small = [[1, 0, 0, 0],
         [0, 4, 1, 0],
         [0, 0, 0, 3],
         [4, 0, 0, 0]]

small2 = [[0, 0, 1, 0],
          [4, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 3, 0, 0]]

big = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [4, 0, 0, 7, 8, 9, 0, 0, 0],
       [7, 8, 0, 0, 0, 0, 0, 5, 6],
       [0, 2, 0, 3, 6, 0, 8, 0, 0],
       [0, 0, 5, 0, 0, 7, 0, 1, 0],
       [8, 0, 0, 2, 0, 0, 0, 0, 5],
       [0, 0, 1, 6, 4, 0, 9, 7, 0],
       [0, 0, 0, 9, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 3, 0, 0, 0, 2]]

big2 = [[7, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [8, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 8],
        [6, 2, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 7, 0],
        [0, 0, 0, 6, 0, 0, 9, 8, 0],
        [0, 0, 0, 0, 2, 7, 3, 0, 0],
        [0, 0, 2, 0, 8, 0, 0, 5, 0]]

big3 = [[0, 0, 8, 1, 9, 0, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 6, 0, 0, 1, 3, 0],
        [0, 0, 6, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 3, 0, 9, 0, 0],
        [0, 1, 0, 4, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 5, 7]]

big4 = [[0, 0, 0, 6, 0, 0, 2, 0, 0],
        [8, 0, 4, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [4, 0, 5, 0, 0, 0, 0, 0, 7],
        [7, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 5, 0, 0, 0, 8],
        [3, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 6, 0]]

giant = [[ 0,  0, 13,  0,  0,  0,  0,  0,  2,  0,  8,  0,  0,  0, 12, 15],
         [ 7,  8, 12,  2, 10,  0,  0, 13,  0,  0, 14, 11,  6,  9,  0,  4],
         [11, 10,  0,  0,  0,  6, 12,  5,  0,  3,  0,  0,  0, 14,  0,  8],
         [ 1,  0,  0,  0, 14,  0,  2,  0,  0,  4,  6,  0, 16,  3,  0, 13],
         [12,  6,  0,  3,  0,  0, 16, 11,  0, 10,  1,  7, 13, 15,  0,  0],
         [ 0, 13,  0,  0,  0, 15,  8,  0, 14,  0,  0,  0,  0, 16,  5, 11],
         [ 8,  0, 11,  9, 13,  0,  7,  0,  0,  0,  0,  3,  2,  4,  0, 12],
         [ 5,  0,  0, 16, 12,  9,  0, 10, 11,  2, 13,  0,  0,  0,  8,  0],
         [ 0,  0,  0,  0, 16,  8,  9, 12,  0,  0,  0,  0,  0,  6,  3,  0],
         [ 2, 16,  0,  0,  0, 11,  0,  0,  7,  0, 12,  6,  0, 13, 15,  0],
         [ 0,  0,  4,  0,  0, 13,  0,  7,  3, 15,  0,  5,  0,  0,  0,  0],
         [ 0,  7,  0, 13,  4,  5, 10,  0,  1,  0, 11, 16,  9,  0, 14,  2],
         [ 0,  2,  8,  0,  9,  0,  0,  0,  4,  0,  7,  0,  0,  5,  0,  0],
         [14,  0,  0,  0, 15,  2, 11,  4,  9, 13,  3,  0, 12,  0,  0,  0],
         [ 0,  1,  9,  7,  0,  0,  5,  0,  0, 11, 15, 12,  0,  0,  0,  0],
         [16,  3, 15,  0,  0, 14, 13,  6, 10,  1,  0,  2,  0,  8,  4,  9]]

giant2 = [[ 0,  5,  0,  0,  0,  4,  0,  8,  0,  6,  0,  0,  0,  0,  9, 16],
          [ 1,  0,  0,  0,  0,  0,  0, 13,  4,  0,  0,  7, 15,  0,  8,  0],
          [13,  0,  0,  0,  0,  7,  3,  0,  0,  0,  0,  9,  5, 10,  0,  0],
          [ 0, 11, 12, 15, 10,  0,  0,  0,  0,  0,  5,  0,  3,  4,  0, 13],
          [15,  0,  1,  3,  0,  0,  7,  2,  0,  0,  0,  0,  0,  5,  0,  0],
          [ 0,  0,  0, 12,  0,  3,  0,  5,  0, 11,  0, 14,  0,  0,  0,  9],
          [ 4,  7,  0,  0,  0,  0,  0,  0, 12,  0, 15, 16,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 14,  0, 15,  0,  6,  9,  0,  0,  0,  0, 12,  0],
          [ 3,  0, 15,  4,  0, 13, 14,  0,  0,  0,  0,  1,  0,  0,  7,  8],
          [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 10,  0,  0,  0,  0],
          [11,  0, 16, 10,  0,  0,  0,  0,  0,  7,  0,  0,  0,  3,  5,  0],
          [ 0,  0, 13,  0,  0,  0,  0,  0, 14,  0, 16, 15,  0,  9,  0,  1],
          [ 9,  0,  2,  0,  0, 14,  0,  4,  8,  0,  0,  0,  0,  0,  0,  0],
          [ 0, 14,  0,  0,  0,  0,  0, 10,  9,  0,  3,  0,  0,  0,  1,  7],
          [ 8,  0,  0,  0, 16,  0,  0,  1,  2, 14, 11,  4,  0,  0,  0,  3],
          [ 0,  0,  0,  1,  0,  0,  5,  0,  0, 16,  0,  6,  0, 12,  0,  0]]

giant3 = [[ 0,  4,  0,  0,  0,  0,  0, 12,  0,  1,  0,  0,  9,  0,  8,  0],
          [15, 14,  0,  0,  9,  0,  0, 13,  8,  0,  0, 10,  1,  0,  0,  0],
          [ 0,  7,  0,  0,  0,  0,  0,  8, 16,  0, 14,  0,  0,  2,  0,  0],
          [ 0,  0,  0,  9,  0,  0, 11,  0,  0,  0,  0,  0,  5,  0,  0, 15],
          [ 3,  0, 12,  0,  7,  0, 10,  0,  0, 11,  2,  0,  0,  0,  0,  6],
          [14,  8,  0,  0,  0, 12,  0,  6,  0,  0,  0, 16,  0,  0,  0, 10],
          [ 0, 16,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12,  0],
          [ 6,  0,  0,  0,  0,  8,  0,  5,  1,  7, 13,  0, 11,  0,  0, 14],
          [ 0,  0,  0,  2,  0,  0, 16,  0, 15, 12,  0,  3, 10,  7,  0,  0],
          [ 0,  9,  0,  5, 11,  0,  3,  0,  4, 13, 16,  0,  0, 15,  6,  0],
          [ 0,  0,  0,  0,  5,  4,  0,  0,  9,  6,  0,  2,  0,  0,  0,  0],
          [ 1,  0,  0,  0,  0, 15, 12,  0,  0,  0,  5,  0,  0,  0,  9,  0],
          [12, 10,  0, 15,  0,  1,  0,  0,  2,  9,  3,  4,  0,  0,  5,  0],
          [ 0,  0,  0,  3, 10,  0,  4,  0,  0, 15,  0,  0,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 16,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 11],
          [11,  6,  8,  0,  0,  0, 15,  0, 14,  0,  0,  0,  0, 13,  0,  2]]

sudokus = [[], [], [small, small2], [big, big2, big3, big4], [giant, giant2, giant3]]

########### Module functions ###########################
from copy import deepcopy

#A: Display Sudoku
def print_board(board):
    """
    Prints a given board to the console in a way that aligns the content of columns and makes
    the subgrids visible.

    Input : a Sudoku board (board) of size 4x4, 9x9, or 16x16
    Effect: prints the board to the console 

    For example:

    >>> print_board(small2)
    -------
    |  |1 |
    |4 |  |
    -------
    |  | 2|
    | 3|  |
    -------
    >>> print_board(big)
    -------------
    |   |   |   |
    |4  |789|   |
    |78 |   | 56|
    -------------
    | 2 |36 |8  |
    |  5|  7| 1 |
    |8  |2  |  5|
    -------------
    |  1|64 |97 |
    |   |9  |   |
    |   | 3 |  2|
    -------------
    >>> print_board(giant2)
    ---------------------
    | 5  | 4 8| 6  |  9G|
    |1   |   D|4  7|F 8 |
    |D   | 73 |   9|5A  |
    | BCF|A   |  5 |34 D|
    ---------------------
    |F 13|  72|    | 5  |
    |   C| 3 5| B E|   9|
    |47  |    |C FG|    |
    |    |E F |69  |  C |
    ---------------------
    |3 F4| DE |   1|  78|
    |    |    |  9A|    |
    |B GA|    | 7  | 35 |
    |  D |    |E GF| 9 1|
    ---------------------
    |9 2 | E 4|8   |    |
    | E  |   A|9 3 |  17|
    |8   |G  1|2EB4|   3|
    |   1|  5 | G 6| C  |
    ---------------------
    """
    k = len(board)
    n = k**0.5
    lst = '-'*int((2 + n-1 + n**2)) #space to store output
    num = 0 #temperory space to store number >10
    board = deepcopy(board)

    #FILTER
    for i in range(len(board)):
        for j in range(len(board[i])):
            for c in range(10,16):
                if board[i][j] == c :
                    board[i][j] = hex(board[i][j])[2:].capitalize()
            if board[i][j] == 16:
                board[i][j] = 'G'
            if board[i][j] == 0:
                board[i][j] = ' '
                
    #ROW            
    for i in range(len(board)): 
        if i%n == 0 and i>0: # row aggregation in the middle
            lst += '\n'+'-'*int((2 + n-1 + n**2))
        lst += '\n|' #new row
        #COLUMN
        for j in range(len(board[i])): 
            lst += str(board[i][j]) #add to list
            if (j+1)%n == 0: #column aggregation
                lst += '|'
                
    lst = lst + '\n'+'-'*int((2 + n-1 + n**2)) #ending aggregation
    print (lst)
    
    
def subgrid_values(board, r, c):
    """
    Input : Sudoku board (board), row index (r), and column index (c)
    Output: list of all numbers that are present in the subgrid of the board related to the
            field (r, c)

    For example:

    >>> subgrid_values(small2, 1, 3)
    [1]
    >>> subgrid_values(big, 4, 5)
    [3, 6, 7, 2]
    >>> subgrid_values(giant2, 4, 5)
    [7, 2, 3, 5, 14, 15]
    """
    k = len(board[0])
    n = round(k**0.5)
    lst = []
    
    if r>=k or c >=k:
        return 'out of bound'
    
    #locate x axis of subgrid
    x1 = r//n*n
    x2 = r//n*n + (n-1)
                    
    #locate y axis of subgrid
    y1 = c//n*n
    y2 = c//n*n + (n-1)
   
    #access to the numbers in the subgrid
    for i in range(int(x1),int(x2)+1):
        for j in range (int(y1),int(y2)+1):
            if board[i][j] not in lst: 
                lst += [board[i][j]]
    
    if 0 in lst: lst.remove(0)
    
    return lst
     
    pass


def options(board, r, c):
    """
    Input : Sudoku board (board), row index (r), and column index (c)
    Output: list of all numbers that player is allowed to place on field (r, c),
            i.e., those that are not already present in row r, column c,
            and subgrid related to field (r, c)

    For example:

    >>> options(small2, 0, 0)
    [2, 3]
    >>> options(big, 6, 8)
    [3, 8]
    >>> options(giant2, 1, 5)
    [2, 5, 6, 9, 11, 12, 16]
    """
    k = len(board[0])
    n = k**0.5
    lst1 = [] #store number cannot be filled
    lst2 = [] #store output

    if r>=k or c >=k:
        return 'out of bound'
    
    subgrid = subgrid_values(board, r, c)
    #add num in column and row into lst1
    for z in range (0,k):
        if board[r][z] not in lst1:
            lst1.append(board[r][z])
        if board[z][c] not in lst1:
            lst1.append(board[z][c])

    #add num in subgrid into lst1
    for i in range(len(subgrid)):
        if subgrid[i] not in lst1:
            lst1.append(subgrid[i])
                
    for z in range(1,k+1):
        if z not in lst1:
            lst2.append(z)
    
    return lst2 
    pass

def check_empty(board):
    """
    Input: Sudoku board
    Output: True if there is empty space
            False if there is no empty space
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return True
    return False

def hint(board):
    """
    Input : Sudoku board
    Output: field, i.e., pair of row and column index, with the minimum
            number of options among all empty-fields
    """
    n = len(board)
    empt = []
    if check_empty(board) == False:
        return None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                empt.append((i,j))
    min_f = empt[0]
    min_opt = options(board,min_f[0],min_f[1])
    for i,j in empt[1:]:
        opt = options(board,i,j)
        if len(opt)<len(min_opt):
            min_f = (i,j)
            min_opt = opt
    return min_f

#B: Implement the rules
def play(board,board_size=2):
    """
    Input : Sudoku board
    Effect: Allows user to play board via console
    """

    #deep copy
    board = deepcopy(board)
    board_r = deepcopy(board)
    board_u = deepcopy(board)
    print_board(board)
    #game start
    
    while True:
        inp = input().split(' ')
        #input
        if len(inp) == 3 and inp[0].isdecimal() and inp[1].isdecimal() and inp[2].isdecimal():
            i = int(inp[0])
            j = int(inp[1])
            x = int(inp[2])
            if i >= len(board) or j >= len(board):
                print('out of range')
            elif board[i][j] != 0:
                print('cell is filled')
            elif x in options(board,i,j):
                board_u = deepcopy(board)
                board[i][j] = x
                print_board(board)
                if check_empty(board) == False: print('solved')
            elif check_empty(board) == False:
                print('solved')
            else:
                print('invalid ans, available options:', options(board,i,j))              
        #new
        elif len(inp)==3 and (inp[0] == 'n' or inp[0] == 'new') and inp[1].isdecimal() and inp[2].isdecimal():
            k = int(inp[1])
            d = int(inp[2])
            if k < len(sudokus) and 0 < d <= len(sudokus[k]):
                board = deepcopy(sudokus[k][d-1])
                board_r = deepcopy(board)
                board_u = deepcopy(board)
                print_board(board)
            else:
                print('board not found')                
        #undo
        elif inp[0] == 'u' or inp[0] == 'undo':
            board = deepcopy(board_u)
            print_board(board)
            
        #restart
        elif inp[0] == 'r' or inp[0] == 'restart':
            board = deepcopy(board_r)
            print_board(board)

        #hint
        elif inp[0] == 'h' or inp[0] == 'help':
            hnt = hint(board)
            print_board(board)
            print(hnt, options(board, hnt[0], hnt[1]))
        
        #inferred
        elif inp[0] == 'i' or inp[0] == 'infer':
            baord_u = deepcopy(board)
            board = inferred(board)
            if check_empty(board) == False: print('solved')
            print_board(board)
            
        #solve:
        elif inp[0] == 's' or inp[0] =='solve':
            board_c = deepcopy(board_r)
            board_c = solve(board_c)
            if len(board_c) > 0:
                print_board(board_c)
                print('solved')
            else:
                print('no solution')

        #generate
        elif inp[0] == 'g' or inp[0] == 'generate' and inp[1].isdecimal():
            k = int(inp[1])
            board = deepcopy(generate(k))
            board_r = deepcopy(board)
            board_u = deepcopy(board)
            print_board(board)
        
        #quit
        elif inp[0] == 'q' or inp[0] == 'quit':
            return        
        else:
            print('Invalid input')
            
########### Functions only relevant for Part II ########
from random import choice
from random import randint

#A: Inference
def value_by_single(board, r, c):
    """
    1st rule:
    if there is only one option in the field,
    the only option must be the answer

    2nd rule:
    if an option of a field can't be filled in the other field (row, column, subgrid)
    the option must be the answer of the field
    
    Input : board, row, and column index
    Output: The correct value for field (i, j) in board if it can be inferred as
            either a forward or a backward single; or None otherwise. 
    
    For example:

    >>> value_by_single(small2, 0, 1)
    2
    >>> value_by_single(small2, 0, 0)
    3
    >>> value_by_single(big, 0, 0)
    """
    k = len(board)
    n = round(k**0.5)
    opt = options(board,r,c)
    opts = []
    optr = []
    optc = []

    #1st rule
    if len(opt) == 0:
        return None
    elif len(opt) == 1:
        return opt[0]

    #2nd rule
    #check options in row & column
    for i in range(k):
        if board[r][i] == 0 or board[i][c] == 0:
            optc += options(board, i, c)
            optr += options(board, r, i)
            
    #check options in subgrid
    for x in range(r//n*n,r//n*n+n):
        for y in range(c//n*n,c//n*n+n):
            if board[x][y] == 0:
                opts += options(board,x,y)
                
    for i in opt:
        if optc.count(i) == 1 or optr.count(i) == 1 or opts.count(i) == 1:
            return i
    else: return None
    pass            
    
def inferred(board):
    """
    implment value_by_single on every empty field
    base case: no more empty cell can be filled with value_by_single
    
    Input : Sudoku board
    Output: new Soduko board with all values field from input board plus
            all values that can be inferred by repeated application of 
            forward and backward single rule

    For example board big can be completely inferred:

    >>> inferred(big) # doctest: +NORMALIZE_WHITESPACE
    [[2, 1, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [1, 2, 4, 3, 6, 5, 8, 9, 7],
    [3, 6, 5, 8, 9, 7, 2, 1, 4],
    [8, 9, 7, 2, 1, 4, 3, 6, 5],
    [5, 3, 1, 6, 4, 2, 9, 7, 8],
    [6, 4, 2, 9, 7, 8, 5, 3, 1],
    [9, 7, 8, 5, 3, 1, 6, 4, 2]]

    But function doesn't modify input board:

    >>> big # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [4, 0, 0, 7, 8, 9, 0, 0, 0],
     [7, 8, 0, 0, 0, 0, 0, 5, 6],
     [0, 2, 0, 3, 6, 0, 8, 0, 0],
     [0, 0, 5, 0, 0, 7, 0, 1, 0],
     [8, 0, 0, 2, 0, 0, 0, 0, 5], 
     [0, 0, 1, 6, 4, 0, 9, 7, 0],
     [0, 0, 0, 9, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 3, 0, 0, 0, 2]]

    In board big4 there is nothing to infer:
    
    >>> inferred(big4) # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0, 6, 0, 0, 2, 0, 0],
     [8, 0, 4, 0, 3, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 9, 0, 0, 0], 
     [4, 0, 5, 0, 0, 0, 0, 0, 7],
     [7, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 3, 0, 5, 0, 0, 0, 8],
     [3, 0, 0, 0, 7, 0, 0, 0, 4],
     [0, 0, 0, 0, 0, 1, 9, 0, 0],
     [0, 0, 0, 2, 0, 0, 0, 6, 0]]
    """
    k= len(board)
    n = round(k**0.5)
    boards = deepcopy(board) #check base case
    board = deepcopy(board) #avoid side effect
    #change state
    for i in range(k):
        for j in range(k):
            if board[i][j]== 0 and value_by_single(board,i,j) != None:
                board[i][j] = value_by_single(board, i, j)
    #base case
    if board == boards or check_empty(board) == False:
        return board
    #call itself
    if check_empty(board):
        return inferred(board)         
    pass

#B: Backtracking
def solve(part):
    """
    optimization:
    1. fill the field with least number of options
    the lesser the available options,
    the higher the of chance of guessing the right answer
    as P(correct answer) = 1/(number of options)
    
    2. inferred the board before fillng the field
    Infferring the board could reducing the steps of
    finding the solution or reaching the deadend
    
    Input: a board
    Output: solution of board
    """
    n = len(part)
    part = inferred(part) #infer
    if check_empty(part)== False:
        return part
    else:
        #choose filed to fill
        hnt = hint(part)
        i, j = hnt[0], hnt[1]
        opt = options(part,i,j)
        if part[i][j] == 0:
            res = []
            for o in opt:
                part_c = deepcopy(part)
                part_c[i][j] = o
                res += solve(part_c)
                if len(res)>0: break #break recursion
            return res

#C: Generate      
def is_unique(part):
    """
    Input: a board
    output: True if it has unique solution
            False if it doesnt have unique solution
            'no solution' if it doesnt have solution
    """

    def check_unique(part,s=[]):
        """
        search first two solution of a sudoku
        base case is when two solution are found  
        Input: a board and an empty list
        Output: a pairs of tuple, ([],solution(s))
                where first element is last found solution
                second elemet is solution(s) of the board
                if board is unique, one solution is return
                if board is not unique, two solution is return
                if board has no solution, []
        """
        n = len(part)
        part = inferred(part)
        if check_empty(part)==False and part not in s:
            s.append(part)
            return part,s
        else:
            hnt = hint(part)
            i, j = hnt[0], hnt[1]
            opt = options(part,i,j)
            if part[i][j] == 0:
                res = []
                for o in opt:
                    part_c = deepcopy(part)
                    part_c[i][j] = o
                    sol = check_unique(part_c,s)
                    res += sol[0]
                    if len(res)>0:
                        res = []
                    s = sol[1]
                    if len(s) >= 2:
                        break
                return res,s
    check = check_unique(part,[])[1]
    if len(check) >=2:
        return False
    elif len(check) == 1:
        return True
    else: return 'no solution' 
        
            
def generate(k):
    """
    steps
    1. create an empty board
    2. form a valid, solved sudoku board
    3. fill field of another empty board base on generated sudoku
       until the board has unique solution
    input: length of sudoku subgrid
    output: a valid sudoku board
    """
    n = k**2
    #create empty list
    board = []
    for r in range(n):
        board.append([])
        for c in range(n):
            board[r].append(0)

    print('generating board...')
    #fill the block
    board_c = deepcopy(board)
    for i in range(n):
        print (str(round((i)/n*100))+'%') # progress
        for j in range(n):
            opt = options(board,i,j)
            board[i][j] = choice(opt)
            while i>0 and len(solve(board)) == 0:
                board[i][j] = choice(opt)
                
    print('99%')
    
    #create template
    for rep in range(n): #minimum number of clues that will always have solution
        x = randint(0,n-1)
        y = randint(0,n-1)
        board_c[x][y] = board[x][y]

    print('loading')
            
    while is_unique(board_c) == False:
        x = randint(0,n-1)
        y = randint(0,n-1)
        while board_c[x][y] > 0:
            x = randint(0,n-1)
            y = randint(0,n-1)         
        board_c[x][y] = board[x][y]

    #print_board(board_c)
    return board_c

########### Driver code (executed when running module) #

import doctest
doctest.testmod()

play(giant2)
