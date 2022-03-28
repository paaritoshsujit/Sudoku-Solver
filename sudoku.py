
#####################################################################
##### Implementing a Sudoku Solver using the BackTrack Technique ####
#####################################################################

from pprint import pprint




def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that is not filled yet --> represented by -1
    # return row, col tuple (or (None, None) if there is none)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None   # if no spaces are empty(-1)




def is_valid(puzzle, guess, row, col):
    # figures out whether the gues of row, col of the puzzle os a valid guess
    # returns True if guess is valid, otherwise False
    
    # we start our checks with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
     # and now for columns

    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]   # list comprehension, easier to read and write
    if guess in col_vals:
        return False

    # now we check for the 3x3 grid in which the square lies
    # this is slightly tricky. we require the start indices for the 3x3 grid. This can be done by:
    row_start = (row//3)*3
    col_start = (col//3)*3

    # now that we have our indices for 3x3 start, we iterate over it to check if the guess is valid
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    return True     # if the guess has passed all the above checks, it is a valid guess



##############################################################
################### Solver Implementation ####################

def solve_sudoku(puzzle):   # puzzle is a list of lists ( i.e. a 2D array)
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return solution

    # Step 1 : choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)  #used to find the next empty square where we shall maker our guess
    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True     # indicates that the sudoku was solved successfully
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1,10):   # i.e. range(1,10) is 1, 2, 3...9
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # step 4: then we recursively call our solver
            if solve_sudoku(puzzle):
                return True

        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number 
        # i.e. we need to backtrack and try the next guess
        puzzle[row][col] = -1   # we reset the guess back to a blank value
            # this means that in the next iteration, the program treats it as a totally new square, and a new guess is assigned to it.

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE
    return False




if __name__ =='__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    print(solve_sudoku(example_board))
    pprint(example_board)  