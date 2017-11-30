# ============================================================
#
# Student Name (as it appears on cuLearn): Michael Balcerzak
# Student ID (9 digits in angle brackets): <101071699>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

'''
This is the make chess board function, have the user to make their own chess board.

@params			none
@return			chessBoardMain, the chess board that was made by the user
'''
def makeChessBoard():

	#print the instructions
	print("put the chess board you want. \nExample input:\n-----k--")
	print("- is an empty spot if no letter is on that spot. \n/ shows that you are moving to the next row of the board. \nThere are 8 rows and 8 columns and each charature you type represent a spot. \nIf the row is empty, then write --------. \nYou first need to type the first row to the last.\nYou need to put 8 chars in each row and press enter to go to the next.")
	print("King(k,K) - 0\nQueen(q,Q) - 10\nRook(r,R) - 5\nKnight(n,N) - 3.5\nBishop(b,B) - 3\nPawn(p,P) - 1\nBlack - Upper case letters\nWhite - lower case letters\nThese letters represent each piece on the board.")

	while True:
		#varibles
		chessBoardMain = []
		badChessBoard = False

		#put each row and see there is no errors
		for counter in range(8):
			chessBoardRow = input("input here row: ")
			if not (len(chessBoardRow) == 8) or chessBoardRow in ['-','/','k','q','r','n','b','p','K','Q','R','N','B','P']:
				badChessBoard = True
			chessBoardMain.append(chessBoardRow)
		
		#check if the user put the board correctly
		if badChessBoard == True:
			print("there are more or less than 8 spots in one of the rows.")
			print("Or you did not put the good values like -,/,k,q,r,n,b,p,K,Q,R,N,B,P. \nPlease put the values again")
		else:
			break
	
	chessBoardList = []

	#make the new chess board
	for row in chessBoardMain:
		col = []
		for block in row:
			col.append(block)
		chessBoardList.append(col)

	#retrun the new chess board
	return chessBoardList

'''
This is the calculate score function, find the scores for each player.

@params			chessBoard, the board that used to caculate the scores
@return			blackScore, the score that the black player have
                	whiteScore, the score that the white player have
'''

def calculateScore(chessBoard):

	#local varibles
	blackScore = 0
	whiteScore = 0

	#go thought the board to find its scores
	for counter in range(len(chessBoard)):
		for counter2 in range(len(chessBoard[counter])):
			if chessBoard[counter][counter2] == 'q':
				whiteScore += 10
			elif chessBoard[counter][counter2] == 'r':
				whiteScore += 5
			elif chessBoard[counter][counter2] == 'n':
				whiteScore += 3.5
			elif chessBoard[counter][counter2] == 'b':
				whiteScore += 3
			elif chessBoard[counter] [counter2] == 'p':
				whiteScore += 1
			elif chessBoard[counter][counter2] == 'Q':
				blackScore += 10
			elif chessBoard[counter][counter2] == 'R':
				blackScore += 5
			elif chessBoard[counter][counter2] == 'N':
				blackScore += 3.5
			elif chessBoard[counter][counter2] == 'B':
				blackScore += 3
			elif chessBoard[counter] [counter2] == 'P':
				blackScore += 1

	#retrun both values
	return blackScore, whiteScore

'''
This is the move piece function, change the location of the piece.

@params			chessBoard, the board that will move a chess piece
@return			chessBoard, the board that moved a chess piece to a new location
'''

def movePiece(chessBoard):
	print("  ABCDEFGH")
	for counter in range(len(chessBoard)):
			print(chr(counter + 65) + " ", end='')
			for counter2 in range(len(chessBoard[counter])):
				print(chessBoard[counter][counter2], end='')
			print('\t')
	while True:
		try:
			#place the coordinates to select the piece you wanted to move
			print("put the row that you want to take. starts from A at the top and ends at H at the bottom.")
			pieceLocationRow = ord(input("Input here: ")) - 65
			print("put the col that you want to take. starts from A at the left and ends at H at the right.")
			pieceLocationCol = ord(input("Input here: ")) - 65
			piece = chessBoard[pieceLocationRow][pieceLocationCol]
			# check if there is a piece located there
			if piece == '-':
				print("no chess piece located here, please find anoter spot\n")
			else:
				#move the piece to a new location
				newLocationRow = ord(input("place the new row location of where the selected piece will be moved. \ninput here: ")) - 65
				newLocationCol = ord(input("place the new col location of where the selected piece will be moved. \ninput here: ")) - 65
				chessBoard[newLocationRow][newLocationCol] = piece
				chessBoard[pieceLocationRow][pieceLocationCol] = '-'

				break

		#check if a row or colum that is out of range
		except IndexError:
			print("you put a row or colum that is out of range (A,H). Please put another number.\n")

	#retrun the new chess board
	return  chessBoard
'''
This is the main function, responsible for the user interface.

@params			none
@return			none
'''

def main():

	#local varibles
	chessBoard = makeChessBoard()
	blackScore, whiteScore = calculateScore(chessBoard)

	#loop though the program
	while True:

		#print the chess board
		for counter in range(len(chessBoard)):
			for counter2 in range(len(chessBoard[counter])):
				print(chessBoard[counter][counter2], end='')
			print('\t')

		#print the instructions
		print("This program finds out how many pieces are on the board and finds out who wins.\nAbove is your chess board that the program is using. \nWrite \"MAKE\" to put your own chess board and calculate its scores. \nWrite \"MOVE\" to change the piece locaton and move it somewhere else. \nWrite \"STOP\" to leave the program\n")
		print("black player's score: ", blackScore)
		print("white player's score: ", whiteScore)

		#tell who wins
		if blackScore > whiteScore:
			print("black player wins")
		elif blackScore < whiteScore:
			print("white player wins")
		else:
			print("tie")
		#input the choose
		usersChoose = input(str("type your choose: ")).upper()

		#choose which function to uses
		if usersChoose == "MAKE":
			chessBoard = makeChessBoard()
			blackScore, whiteScore = calculateScore(chessBoard)
		elif usersChoose == "MOVE":
			chessBoard = movePiece(chessBoard)
			blackScore, whiteScore = calculateScore(chessBoard)
		elif usersChoose == "STOP":
			print("You exit your program")
			break

main()

