from test import *
from time import *
board = [
        ["1","2","3"],
        ["4","5", "6"],
        ["7", "8", "9"]
        ]
text = """
 /$$$$$$$$ /$$$$$$  /$$$$$$        /$$$$$$$$ /$$$$$$   /$$$$$$        /$$$$$$$$ /$$$$$$  /$$$$$$$$
|__  $$__/|_  $$_/ /$$__  $$      |__  $$__//$$__  $$ /$$__  $$      |__  $$__//$$__  $$| $$_____/
   | $$     | $$  | $$  \__/         | $$  | $$  \ $$| $$  \__/         | $$  | $$  \ $$| $$      
   | $$     | $$  | $$               | $$  | $$$$$$$$| $$               | $$  | $$  | $$| $$$$$   
   | $$     | $$  | $$               | $$  | $$__  $$| $$               | $$  | $$  | $$| $$__/   
   | $$     | $$  | $$    $$         | $$  | $$  | $$| $$    $$         | $$  | $$  | $$| $$      
   | $$    /$$$$$$|  $$$$$$/         | $$  | $$  | $$|  $$$$$$/         | $$  |  $$$$$$/| $$$$$$$$
   |__/   |______/ \______/          |__/  |__/  |__/ \______/          |__/   \______/ |________/
                                                                                                     
                                                                                                       """

is_player_one = True
print(text)

print("Hello and welcome to the Tic Tac Toe game for 2 players.\nPlayer 1 will have the 'X' symbol and player 2 will have the 'O' symbol")
print("Here is your board:")
pretty_board_printer(board)

while not victory_tic_tac_toe(board) and not draw(board):
        if is_player_one:
                choice = int(input("The player 1 has the hand : "))
                while choice >9 or choice < 1 :
                        choice = int(input("Please choose a number between 1 and 9: "))
                while not tic_tac_toe(board, int(choice), "X"):
                        choice = input("This choice was already made. Please Retry : ")
                pretty_board_printer(board)
                is_player_one = not is_player_one
        else:
                choice = int(input("The player 2 has the hand : "))
                while choice >9 or choice < 1 :
                        choice = int(input("Please choose a number between 1 and 9: "))
                while not tic_tac_toe(board, int(choice), "O"):
                        choice = input("This choice was already made. Please Retry : ")
                pretty_board_printer(board)
                is_player_one = not is_player_one

if is_player_one and not draw(board):
        print("Congratulations Player 2. You won tha game : )")
elif not is_player_one and not draw(board):
        print("Congratulations Player 1. You won tha game : )")
elif draw(board):
        print("The game ends in a draw :/")

sleep(6)
