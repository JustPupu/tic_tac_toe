''' This program runs the tic tac toe game.
You can choose to play either with computer or with the other player.
'''

import random 

SEPARATOR = '='*50

RULES = '''
GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row
'''

def rules():
	''' Rules of the game'''
	return print(SEPARATOR + RULES)

# *******************************************************************
# BUILDING THE BOARD

def visual_board(board):
	''' Visualisation of the board on screen'''
	print(board[0] + ' | ' + board[1] + ' | ' + board[2])
	print('—' * 10)
	print(board[3] + ' | ' + board[4] + ' | ' + board[5])
	print('—' * 10)
	print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# *******************************************************************
# THE BOARD SLICES FOR WIN-CHECK
# If 'return' follows, then 'elif' or 'else' has no meaning

def nth_row(board, i):
	'''Returns n-th row from the board'''
	if i == 1:
		return board[:3]
	if i == 2:
		return board[3:6]
	if i == 3:
		return board[6:]

def nth_column(board, i):
	'''Returns n-th column from the board'''
	if i == 1:
		return board[0::3]
	if i == 2:
		return board[1::3]
	if i == 3:
		return board[2::3]

def diagonal(board, i):
	'''Returns a diagonal from top left or from top right'''
	if i == 'left':
		return [board[0], board[4], board[8]]
	if i == 'right':
		return [board[2], board[4], board[6]]

# *******************************************************************
# FUNCTIONS FOR COMPUTER VERSION

def whos_who():
	'''Allows user to choose X or O'''
	inp = ''
	while inp != "X" and inp != "O":
		inp = input("Would you like to be X or O: ").upper()
		if inp != "X" and inp != "O":
	  		print("You must type X or O.")
	if inp == "X":
		return "X", "O"
	return "O", "X"

def computer_turn(board):
	'''Makes move as a computer'''
	while True:
		move = random.randint(1,9)
		if str(move) not in board:
			continue
		return move 

# *******************************************************************
# MAIN GAME FUNCTIONS

def choose_game():
	'''Allows user to choose what type of game wants to play'''
	board = [str(i) for i in range(1,10)]
	inp = ''
	while inp != "y" and inp != "n":
		inp = input("Would you like to play with a computer? y/n: ").lower()
		if inp != "y" and inp != "n":
	  		print("You must type y or n.")
	if inp == "y":
		play_comp(board)
	else:  # Only two options, so there is no need for another condition
		two_players(board)

def read_players_move(board, turn):
	'''Checks validity of given turn'''
	while True:
		print(SEPARATOR)
		pl_move = input(f'Player {turn} | Please enter your move number:\n')

		# 'Show rules' choice
		if pl_move == 'r':
			print(RULES)
			continue
		# Checks if input is an integer
		try:
			move = int(pl_move)	
		except ValueError:
			print('You must enter a whole number between 1 and 9.')
			continue
		# Checks if given number is between 1-9
		if not 0 < move < 10:
			print('Please enter the number between 1 an 9.')
			continue
		# Checks if the spot is not already taken
		if str(move) not in board:
			print('That spot is already taken.')
			continue
		return move  # Have to indent into while loop for exiting it
			    	 # otherwise you'll stay in the loop forever

def is_winner(board, turn):
	'''Checks if there is a winner'''
	win = [turn for t in range(3)]  # XXX or OOO for compare
	for r in range(1,4):  # Three rows and columns

		# Checks Xs and Os across the rows
		if nth_row(board, r) == win:
			return True
		# Checks Xs and Os across the columns
		elif nth_column(board, r) == win:
			return True
	
	# Checks Xs and Os across diagonals				
	if diagonal(board, 'left') == win:
		return True
	elif diagonal(board, 'right') == win:
		return True
	return False

def two_players(board):
	'''Game for two players'''
	turn = 'X'  # Player X starts the game

	# After 9 moves the board is full, hence the result is "tie"
	for i in range(9): 
		visual_board(board)
		move = read_players_move(board, turn)

		board[move-1] = turn  # Imprints a succesfull move into the board

		# After 5th turn starts to check if anyone won
		if i >=4:
			check_win = is_winner(board, turn)
			if check_win is True:
				visual_board(board)
				return print(f'Congratulations, the player {turn} won in {i+1}. turn.')

		# Changes the player after every move
		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'

	else:  # Syntax sugar
		visual_board(board)
		print('It\'s a tie!')

def play_comp(board):
	'''Game for player vs. Computer'''
	turn = 'X'  # Player X starts the game
	player, computer = whos_who()

	# After 9 moves the board is full, hence the result is "tie"
	for i in range(9): 
		visual_board(board)
		if turn == computer:
			move = computer_turn(board)  # Makes move as a computer if it's its turn
			print(SEPARATOR)
			print(f'Computer ({computer}) chose to make a move no. {move}.')
		else: 
			move = read_players_move(board, turn)

		board[move-1] = turn  # Imprints a succesfull move into the board

		# After 5th turn starts to check if anyone won
		if i >=4:
			check_win = is_winner(board, turn)
			if check_win is True:
				visual_board(board)
				return print(f'Congratulations, the player {turn} won in {i+1}. turn.')

		# Changes the player after every move
		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'

	else:  # Syntax sugar
		visual_board(board)
		print('It\'s a tie!')	

def play_again():
	'''Asks player to play again'''
	inp = ''
	while inp != "y" and inp != "n":
		inp = input("Would you like to play again? y/n: ").lower()
		if inp != "y" and inp != "n":
	  		print("You must type y or n.")
	if inp == "y":
		return True
	return False

# *******************************************************************
# BUILDING THE CODE

def main():
	print('Welcome to Tic Tac Toe!')
	rules()
	print('(To show rules during the game, please enter "r")')
	print('Let\'s start the game:\n' + SEPARATOR)

	while True:
		choose_game()
		if play_again():
			continue
		return print('Exiting...')

if __name__ == "__main__":
	main()