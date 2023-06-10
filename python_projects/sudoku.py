
#helper function to find next empty spot
def find_next_spot(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]=="-1":
                return r,c

    return None,None

#helper function to determine if guess for a spot is valid
def is_valid(puzzle,guess,row,column):

    #1. check the rows
    for i in range(9):
        if puzzle[row][i] == guess:
            return False

    #2. check the columns
    for i in range(9):
        if puzzle[i][column] == guess:
            return False

    #3. check the subgrid
    # which block of rows the spot is in
    row = row//3
    #which block of columns the spot is in
    column = column%3

    for r in range(row*3,(row+1)*3):
        for c in range(column*3,(column+1)*3):
            if puzzle[r][c]==guess:
                return False

    return True


def solve(puzzle):


    # step 1: choose empty spot on puzzle to make a guess
    # using a helper function
    row,column = find_next_spot(puzzle)


    #if there are no more empty spots, that means that the puzzle is solved
    # as we will be validating the guess on each empty spot
    if row is None:
        return True

    # step 2: make a guess between 1 and 9 for the empty spot chosen
    for guess in range(9):
        if is_valid(puzzle,guess,row,column):
            puzzle[row][column] = guess

            #recurse to continue the game, continue guessing and assigning guesses to spots if guesses are valid
            if solve(puzzle):
                return True

            #if puzzle cannot be solved using current guess for current spot, reset
            else:
                puzzle[row][column]='-1'

        #if guess is not valid, skip and try the next guess
        else:
            continue

    #if all the combinations don't work, puzzle is unsolvable
    return False

if __name__ == "__main__":
    puzzle = [
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
    print(solve(puzzle))
    print(puzzle)


