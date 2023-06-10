import math
import random

class Player:

    #constructor method to initialize the object(player)'s attributes
    def __init__(self,letter):
        self.letter = letter

    #method for player's next move
    def get_move(self,game):
        pass

#using inheritance of OOP to create computer player based on base player object
class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)


    def get_move(self,game):

        #randomly chooses any position or spot that is empty and returns the index
        square = random.choice(game.available_moves())
        return (square)

#using inheritance of OOP to create human player based on base player object
class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + " 's turn. Input move (0-8):")
            try:
                value = int(square)

                # if user did not enter an index of an empty spot
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                print('Invalid square. Try again please')

        return value

class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        """
        function that returns the square player wants to make a move on
        """

        #randomly select a square if all the squares are empty
        if (len(game.available_moves())==9):
            square = random.choice(game.available_moves())
            return square

        #else, use minimax algorithm to select square to maximize chances of winning
        else:
            square = self.minimax(game,self.letter)["Position"]
            return square

    def minimax(self,state,Player):
        """
        recursive function using utility function to determine next move
        """
        max_player = self.letter
        other_player = "O" if max_player == "X" else "X"

        #base case 1
        # if winner exists, terminate recursion and return a dictionary with position and score
        if state.current_winner:
            return {"Position":None,
                    "Score": 1*(len(state.available_moves())+1) if state.current_winner == max_player else
                    -1*(len(state.available_moves())+1)
            }
        #base case 2
        # if there's a tie
        elif not state.empty_squares():
            return {"Position":None,
                    "Score":0
            }

        # initializing a dictionary that saves the best position and best score for max_player
        if Player == max_player:
            best = {"Position": None,
                    "Score": -math.inf}

        #initializing a dictionary that saves the best position and best score for other_player
        else:
            best = {"Position": None,
                    "Score": math.inf}

        #recursive case to loop through all possible moves
        for possible_move in state.available_moves():

            #step 1: make a move, try that spot
            state.make_move(possible_move,Player)

            #step 2: recurse using minimax to simulate game after that move
            simulation = self.minimax(state, other_player)

            #step 3: undo the move
            state.board[possible_move] = " "
            state.current_winner = None
            simulation["Position"] = possible_move

            #update best dictionary
            if Player==max_player and simulation["Score"]>best["Score"]:
                best = simulation

            if Player==other_player and simulation["Score"]<best["Score"]:
                best = simulation

        #returning best dictionary with best next position to take and best score
        return best



