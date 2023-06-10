#This is a minesweeper game

import random

#creating a class board in python
class Board:
    def __init__(self,dim_size,num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #creating the board with a helper function
        self.board = self.make_new_board()

        self.assign_values_to_spot()

        #initializing a set to keep track of which locations we have dug
        #we'll save (row,column) tuples into this set
        self.dug = set()


    def make_new_board(self):
        #construct a new board based on dim_size and num_bombs
        board = [[None for i in range(self.dim_size)] for j in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted<self.num_bombs:
            index = random.randint(0,self.dim_size**2-1)
            row = index//self.dim_size
            column = index%self.dim_size

            if board[row][column] == '*':
                continue
            else:
                board[row][column] = '*'
                bombs_planted +=1
        return board


    # function that assigns number of neighbouring bombs for each spot
    def assign_values_to_spot(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c]=='*':
                    continue
                else:
                    self.board[r][c]=self.get_num_neighbouring_bombs(r,c)

    # function that calculates number of neighbouring bombs for each spot
    def get_num_neighbouring_bombs(self,row,column):

        #iterating through 3 by 3 spots around current spot
        num = 0
        for r in range(max(0,row-1), min(self.dim_size,row+2)):
            for c in range(max(0,column-1),min(self.dim_size,column+2)):
                if r==row and c==column:
                    continue
                if self.board[r][c]=='*':
                    num +=1
        return num

    def dig(self, row, col):
        #dig at a location, return True if successful dig, False if bomb dug

        #a few scenarios
        #hit a bomb ->game over
        #dig at location with neighbouring bombs -> finish dig
        #dig at location with no neighbouring bombs -> recursively dig neighbours


        #add to self.dug set to track positions we have dug
        self.dug.add((row,col))

        if self.board[row][col]=='*':
            return False
        elif self.board[row][col]>0:
            return True

        else:

            #if self.board[index] == 0, recursively dig neighbours
            for r in range(max(0,row-1), min(self.dim_size,row+2)):
                for c in range(max(0,col-1),min(self.dim_size,col+2)):
                    if (r,c) in self.dug:
                        continue
                    self.dig(r,c)

        return True

    def __str__(self):

        visible_board = [[None for i in range(self.dim_size)] for j in range(self.dim_size)]
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if (r,c) in self.dug:
                    visible_board[r][c] = self.board[r][c]
                else:
                    visible_board[r][c] = " "

        return '\n'.join(['|'.join([str(cell) for cell in row]) for row in visible_board])





#play the game
def play(dim_size=10,num_bombs=10):
    #step 1: create the board and plant the bombs
    board = Board(dim_size,num_bombs)

    #step 2: show user the board and ask them where they want to dig
    #step 3: if location is a bomb, print game over message
    #step 4: if location is not a bomb, dig recursively until each square is at least next to a bomb
    #step 5: if all the squares (that are not bombs) have been dug, user has won

    while len(board.dug)<board.dim_size**2 - num_bombs:
        print(board)
        dig_location = input("Where do you want to dig? Input your location as row,column: ")
        row_str,column_str = dig_location.split(",")
        row,column = int(row_str),int(column_str)

        if row<0 or row>=dim_size or column<0 or column>=dim_size:
            print("Location not valid. Try again")
            dig_location = input("Where do you want to dig? Input your location as row,column: ")
            row_str,column_str = dig_location.split(",")
            row,column = int(row_str),int(column_str)

        #if board.dig() returns False
        if not board.dig(row,column):
            print("Bomb! Game over rip!")
            #reveal the whole board
            #assigning all possible (row,col) values into board.dug, so that in __str__(self) function, visible_board[r][c] = self.board[r][c] for all possible (row,col) values
            board.dug =[(r,c)for r in range (board.dim_size) for c in range(board.dim_size)]
            print(board)
            break

    if len(board.dug) == board.dim_size**2 - num_bombs:
        print("congrats!you have won!")



if __name__ == "__main__":
    play(10,10)












    #def print_board(self):
        #for row in [self.board[i*self.dim_size:(i+1)*self.dim_size] for i in range(self.dim_size)]:
            #print('|' + '|'.join(row) + '|')

