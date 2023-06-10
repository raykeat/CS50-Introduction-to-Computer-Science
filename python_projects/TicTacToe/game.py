from player import RandomComputerPlayer, HumanPlayer, GeniusComputerPlayer
#from player.py file import classes RandomComputerPlayer, HumanPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' +' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]

        for row in number_board:
             print('| ' +'|'.join(row) + ' |')


    def available_moves(self):
        """
        function that returns a list of indexes of spots/positions which are empty
        """

        #using list comprehension
        return [i for (i,spot) in enumerate(self.board) if spot == ' ']

        #moves = []

        #enumerate creates a list and assigns tupples with (index,value at index)
        #for (i,spot) in enumerate (self.board):

            # ['x','x','o'] --> [(0,'x'),(1,'x'),(2,'o')]

            #if spot == ' ':
                #moves.append(i)

        #return moves

    def empty_squares(self):
        """
        boolean function encapsulated within tictactoe class that checks if there are still any empty squares
        """
        if len(self.available_moves()) == 0:
            return False
        return True

    def num_empty_squares(self):
        return self.board.count(' ')

    def winner(self,square,letter):
        """
        function to check if winner exists
        """
        #check the row
        row_index = square//3
        row = self.board[row_index*3:(row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True

        #check the column
        column_index = square%3
        column = [self.board[column_index + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check the 2 diagonals
        diagonal1 = [self.board[i] for i in [0,4,8]]
        diagonal2 = [self.board[i] for i in [2,4,6]]
        if all([spot == letter for spot in diagonal1]):
            return True
        if all([spot == letter for spot in diagonal2]):
            return True
        return False


    def make_move(self,square,letter):
        """
        function that assigns letter to the square in the board
        """

        if self.board[square] == ' ':
            self.board[square]=letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False


def play(game, xplayer, oplayer, print_game = True):
    if print_game:
        game.print_board_nums()

    #assigning starting letter
    letter = 'X'

    #iterating while the game still has empty spots

    while game.empty_squares():

        if letter == 'X':
            square = xplayer.get_move(game)
        else:
            square = oplayer.get_move(game)

        #function to actually place player's letter in square
        if game.make_move(square,letter):
            if print_game:
                print(letter,f' makes a move to square {square}')
                game.print_board()

        #stop the game if winner exists
        if game.current_winner:
            if print_game:
                print(letter,' wins!')
            return letter

        time.sleep(2)

        #alternate players using ternary operator
        letter = 'O' if letter=='X' else 'X'

    if print_game:
        print("It's a tie bitch!")


if __name__=='__main__':
    xplayer = GeniusComputerPlayer('X')
    oplayer = HumanPlayer('Y')
    game = TicTacToe()
    play(game, xplayer, oplayer, print_game = True)