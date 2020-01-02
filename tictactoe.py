
#Game Board

board = ["-", "-", "-",
		"-", "-", "-",
		"-", "-", "-",]

#If the Game is still going on
gameIsOngoing = True

#who's the winner
winner = None 

#Whos turn is it
currentPlayer = "x"

def displayBoard():
	print(board[0] + " | "  + board[1] + " | " + board[2] )
	print(board[3] + " | "  + board[4] + " | " + board[5] )
	print(board[6] + " | "  + board[7] + " | " + board[8] )

#Play a game of tictac toe
def playGame():
	#display initial game board
	displayBoard()
	while gameIsOngoing:
		global winner 

		#Handles a single turn of a player
		handleTurn(currentPlayer)

		#check if the game has ended
		#Game over returns winner and turns gameIsOngoing to false
		#thereby breaking out of the loop
		checkGameOver()
		
		#Flip to the other player
		flipTurn()

	#The Game has ended
	if winner == "x" or winner == "o":
		print(winner + " won.")
	elif winner == None:
		print("Tie ")

#Handles  a single turn of an arbitrary player
def handleTurn(player):
	ptn = int(input("Choose a position from 1 to 9: ")) -1
	board[ptn] = "x"
	displayBoard()

def checkGameOver():
	checkIfWin()
	checkIfTie()

def checkIfWin():
	#set up global variables
	global winner

	#check rows will return true or false and assign 
	# it to rowWinner
	rowWinner = checkRows()
	
	#check columns
	columnWinner= checkColumns()

	#check diagonals
	diagonalWinner= checkDiagonals()

	if rowWinner =="x":
		#if rowWinner is true, 
		# winner is true 
		winner = rowWinner
	elif columnWinner:
		#there was a winner
		winner=columnWinner
	elif diagonalWinner:
		#there was a winner
		winner = diagonalWinner
	else :
		#no win
		winner = None
	return

def checkRows():
	global gameIsOngoing
	#setup global variables

	#check if any of the rows have same values and is not a dash
	row1 = board[0] == board[1] == board[2] != "-"
	row2 = board[3] == board[4] == board[5] != "-"
	row3 = board[6] == board[7] == board[8] != "-"

	if row1 or row2 or row3 :
		#i.e if they are all true, Then this shows that theres a win
		gameIsOngoing = False 
	#return the winner, X or O
	if row1:
		return board[0]
	elif row2:
		return board[3]
	elif row3:
		return board[6]
	return

def checkColumns():
	global gameIsOngoing
	#setup global variables

	#check if any of the column have same values and is not a dash
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"

	if column_1 or column_2 or column_3 :
		#i.e if they are all true, Then this shows that theres a win
		gameIsOngoing = False 
	#return the winner, X or O
	if column_1:
		return board[0]
	elif column_2:
		return board[1]
	elif column_3:
		return board[2]
	return

def checkDiagonals():
	global gameIsOngoing
	#setup global variables

	#check if any of the columns have same values and is not a dash
	diagonal_1 = board[0] == board[4] == board[8] != "-"
	diagonal_2 = board[6] == board[4] == board[2] != "-"
	
	if diagonal_1 or diagonal_2:
		#i.e if they are all true, Then this shows that theres a win
		gameIsOngoing = False 
	#return the winner, X or O
	if diagonal_1:
		return board[0]
	elif diagonal_2:
		return board[6]
	return

def checkIfTie():
	return

def flipTurn():
	return

playGame()
