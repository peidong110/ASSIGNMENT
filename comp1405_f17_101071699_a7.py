# ============================================================
#
# Student Name (as it appears on cuLearn): Michael Balcerzak
# Student ID (9 digits in angle brackets): <101071699>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

'''
This function will load a text file.

@params		file_name, the name of the file to be loaded
@return		an uppercase string containing the data read from the file
'''
def load_text(file_name):
	try:
		file_hnd1 = open(file_name, "r")
		file_data = file_hnd1.read()
		file_hnd1.close()
		return file_data.upper()
	except IOError:
		print("I can't find a file called", file_name)
		return ""
'''
This function will save data to a text file.

@params		file_name, the name of the file to be saved
                file_data, the data to be written to the file
@retrun 	none
'''
def save_text(file_name, file_data):
	try:
		file_hnd1 = open(file_name, "w")
		file_hnd1.write(file_data)
		file_hnd1.close()
	except IOError:
		print("I can't find a file called", file_name)
		return ""
'''
This function will encode the user's filename

@params		initialText, the file that is used to be encoded
		alphabet, the encoder that is used to encode the file
@retrun 	currentText, the file that was encoded
'''
def encode(initialText, encoder):

	# local varibles
	mainAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	newText = ""

	# make the encoded text
	for counter in initialText:
		checkLetter = True
        	# put a new letter
		for counter2 in range(26):
			if counter == mainAlphabet[counter2] and checkLetter:
			        newText += encoder[counter2]
			        checkLetter = False
		# make a punctuation
		if checkLetter == True:
			newText += counter

	# returns the encoded text
	return newText
'''
This function will decode the user's filename

@params			initialText, the file that is used to be decoded
                	alphabet, the encoder that is used to encode the file
@retrun 		currentText, the file that was encoded
'''
def decode(currentText, encoder):

	# local varibles
	mainAphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	newText = ""

	# make the initial text
	for counter in currentText:
		checkLetter = True
		# put a new letter
		for counter2 in range(26):
			if counter == encoder[counter2] and checkLetter:
				newText += mainAphabet[counter2]
				checkLetter = False
		if checkLetter == True:
			newText += counter

	# returns the old text
	return newText
'''
This function will move the letters around the encoder

@params			sipherNumber, how many letter will be shifted
@retrun 		alphabet, the encoder that was edded
'''

def caesar_cipher_alphabet(sipherNumber):

	# local varibles
	mainAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	newAlphabet = ""
	newAlphabetNumber = sipherNumber

	# take out the letters from the begining
	while newAlphabetNumber < len(mainAlphabet):
		newAlphabet += mainAlphabet[newAlphabetNumber]
		newAlphabetNumber += 1

	# put the shifted letters at the end
	for counter in range(sipherNumber):
		newAlphabet += mainAlphabet[counter]

	# returns the new alphabet
	return newAlphabet
'''
This function will put letters the user input

@params			sipherString, the string that will be inserted in the encoder
@retrun 		newAlphabet, the string that is modefide
'''
def keyword_cipher_alphabet(sipherString):

	# local varibles
	mainAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	sipherString = sipherString.upper()
	correctString = ""

	# this prosses will remove letters that are 2 or more
	for counter in sipherString:
		for counter2 in mainAlphabet:
			if counter2 == counter and not (counter in correctString):
				correctString += counter

    	# make the new encoder with the users input
	for counter in mainAlphabet:
		if not (counter in correctString):
			correctString += counter

    	# returns the modified encoder
	return correctString
'''
This function will alow the user to make their own ecription key

@params			none
@retrun 		alphabet, the string that the user made
'''
def cryptogram_alphabet():

    	#have all local varibles for this function
	mainAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	newAlphabet = str(input("what encoder you want to inport? "))
	newAlphabet = newAlphabet.upper()
	goodEcriptedCode = True

    	# this prosses checks if the user put a string that has all characters and have only one
	for counter in mainAlphabet:
		numberOfLetters	= 0
		for counter2 in newAlphabet:
			if counter2 == counter:
				numberOfLetters += 1
		if not numberOfLetters == 1:
			print("There are missing or more Letters in the sentence. \nYou need only to put one letter in the sentence.")
			goodEcriptedCode = False

    	# returns the modified encoder if it doesn't have missing or more letters
	if goodEcriptedCode:
		return newAlphabet
	else:
		return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
'''
This is the main function, responsible for the user interface.

@params			none
@return			none
'''
def main():

    	# have all the main varible made
	initialText = ""
	currentText = ""
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	while True:

        	# display all the instruction and the initial and current text
		print("The initial Text is " + initialText)
		print("The current Text is " + currentText)
		print("This program helps you to encode and decode messages. \nType \"load\" to load a file in the program. \nType \"save\" to save the file. \nType \"encode\" to encode your file.")
		print("Type \"decode\" to change the file back. \nType \"caesar\" to move selected letters to the end. \nType \"keyword\" to insert a word.")
		print("Type \"change\" to type your own encoder. \nType \"exit\" to exit the program")

        	# have the user choose the choose
		option = str(input(""))

        	# list of options shown when the user picks one
		if option.upper() == "LOAD":
			fileName = str(input("Put your own file name in the program. "))
			initialText = load_text(fileName)

		elif option.upper() == "SAVE":
			fileName = str(input("Put your created file to save it in your hardrive. "))
			save_text(fileName, currentText)

		elif option.upper() == "ENCODE":
			currentText = encode(initialText, alphabet)

		elif option.upper() == "DECODE":
			currentText = decode(currentText, alphabet)

		elif option.upper() == "CAESAR":
			sipherNumber = int(input("How many letter you want to be shifted. "))
			alphabet = caesar_cipher_alphabet(sipherNumber)

		elif option.upper() == "KEYWORD":
			sipherString = str(input("what string you want to insert to the encoder. "))
			alphabet = keyword_cipher_alphabet(sipherString)

		elif option.upper() == "CHANGE":
			alphabet = cryptogram_alphabet()

		elif option.upper() == "EXIT":
			print("you had exit the program. ")
			break

		else:
			print("That was a invalid text or a spelling mistake. Please type your answer again")

# this is the only line in your code that isn't inside a function definition
main()
