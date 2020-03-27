import random
# Started on 3/26/2020 6:36 PM, finished on 3/26/2020 8:47 PM.

# THE CODE IS CURRENTLY FUNCTIONAL AND MESSY, NOT OPTIMIZED YET!
# CHANGE TO ALL CAPS
#Add user input!
#input() for each word, then figure out how to escape: If input is generate, do it, if the input it a word, append it the the words array

# CHANGE THESE ---------------
SIZE = 15 
words = ['Ackee','Apple','Apricot','Avocado','Banana','Bilberry','Blackberry','Blackcurrant','Black sapote','Blueberry','Boysenberry','Breadfruit','Buddha','Cactus pear','Crab apple','Currant','Cherry','Cherimoya','Chico fruit','Cloudberry','Coconut','Cranberry','Damson','Date','Dragonfruit']
#-----------------------------

wsArray = []
COLS, ROWS = SIZE, SIZE

for rows in range(ROWS):
	thisRow = []

	for cols in range(COLS):
		thisRow.append(' ')

	wsArray.append(thisRow)


alphebet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def print_array(array):
	for i in range(ROWS):
		print(array[i])


def positionInArray(coordinates): # [c, r]
	colPos = coordinates[0]
	rowPos = coordinates[1]

	if colPos >= 0 and colPos <= COLS-1 and rowPos >= 0 and rowPos <= ROWS-1:
		return True
	else: return False


def testForNoVal(coordinates, letter): # [c, r], array
	global wsArray
	colPos = coordinates[0]
	rowPos = coordinates[1]
	letConversion = "'" + letter + "'"

	if positionInArray(coordinates):
		# if wsArray[rowPos][colPos] != ' ':
		# 	return False
		if str(wsArray[rowPos][colPos]) != str(letter) and wsArray[rowPos][colPos] != ' ':
			return False
		if str(wsArray[rowPos][colPos]) == str(letter):
			# It is okay to place here...
			#print(str(wsArray[rowPos][colPos]) + " is equal to" + str(letter))
			return True
		elif wsArray[rowPos][colPos] == ' ':
			# It is okay to place here...
			return True


def getNewCoords(coordinates, direction):
	newC = coordinates[0] + direction[0]
	newR = coordinates[1] + direction[1]
	newCoords = [newC, newR]

	return newCoords
	global mazeArray
	possDirList = [[0, -1], [0, 1], [-1, 0], [1, 0]] # U, D, L, R

	# Dont use direction (filter it out).
	for elem in possDirList:
		if elem == direction:
			possDirList.remove(elem)

	# Dont use direction (filter it out). You may run into problems of the range not working, but it should always be the four directions minus the one passed through.
	for i in range(4-1):

		if positionInArray(getNewCoords(coordinates, possDirList[i])) and not testForVal(getNewCoords(coordinates, possDirList[i])):
			possDirList[i] = 0
		
		elif not testForEdge(getNewCoords(coordinates, possDirList[i])):
			possDirList[i] = 0

		
	newList = list(filter(lambda x: (x != 0), possDirList))

	# Should only leave the valid directions
	return newLis


def inputWord(wordGiven):
	global wsArray
	startRow = 0
	startCol = 0
	wordLength = len(wordGiven) # Not -1?
	directions = [[-1, -1],[0, -1],[1, -1],[-1, 0],[1, 0],[-1, 1],[0, 1],[1, 1]] # [c,r] - NW,N,NE W E SW,S,SE

	# Change this back, if it is possble, set it to thisDirection and break----------------------
	for d in range(len(directions)-1):
		if directions[d] == [-1, -1]:
			if not positionInArray([startCol-wordLength, startRow-wordLength]):
				directions[d] = 0
		elif directions[d] == [0, -1]:
			if not positionInArray([startCol, startRow-wordLength]):
				directions[d] = 0
		elif directions[d] == [1, -1]:
			if not positionInArray([startCol+wordLength, startRow-wordLength]):
				directions[d] = 0
		elif directions[d] == [-1, 0]:
			if not positionInArray([startCol-wordLength, startRow]):
				directions[d] = 0
		elif directions[d] == [1, 0]:
			if not positionInArray([startCol+wordLength, startRow]):
				directions[d] = 0
		elif directions[d] == [-1, 1]:
			if not positionInArray([startCol-wordLength, startRow+wordLength]):
				directions[d] = 0
		elif directions[d] == [0, 1]:
			if not positionInArray([startCol, startRow+wordLength]):
				directions[d] = 0
		elif directions[d] == [1, 1]:
			if not positionInArray([startCol+wordLength, startRow+wordLength]):
				directions[d] = 0

	newList = list(filter(lambda x: (x != 0), directions))
	random.shuffle(newList)
	thisDirection = newList[0]

	#-----------------------------------------------------------------------------------------

	thisIsOkay = False
	toAdd = []
	printWord = []
	letterArray = []

	for let in range(wordLength):
		letterArray.append(wordGiven[let])

	for attempts in range(100):
		if not thisIsOkay:
			toAdd = []

		startRow = random.randint(0, ROWS-1)
		startCol = random.randint(0, COLS-1)
		
		for i in range(wordLength):
			letterList = []
			for n in range(len(toAdd)):
				letterList.append(toAdd[n][1])

			if thisIsOkay and len(toAdd) == len(wordGiven) and letterList == letterArray:
				printWord = []
				for a in range(len(toAdd)):
					lilC = toAdd[a][0][0]
					lilR = toAdd[a][0][1]
					lilLetterToPlace = toAdd[a][1]
					wsArray[lilR][lilC] = lilLetterToPlace
					printWord.append(lilLetterToPlace)
				break
				break

			if wordLength <= ROWS or  wordLength <= COLS:
				if positionInArray([startCol, startRow]) and testForNoVal([startCol, startRow], wordGiven[i]):
					if thisDirection == [-1, -1]:
						thisC = [startCol-i, startRow-i]
						if positionInArray([startCol-wordLength, startRow-wordLength]) and testForNoVal(thisC, wordGiven[i]):
							toAdd.append([thisC, wordGiven[i]])
							if i+1 == wordLength:
								thisIsOkay = True
					elif thisDirection == [0, -1]:
						thisC = [startCol, startRow-i]
						if positionInArray([startCol, startRow-wordLength]) and testForNoVal(thisC, wordGiven[i]):
							toAdd.append([thisC, wordGiven[i]])
							if i+1 == wordLength:
								thisIsOkay = True
					elif thisDirection == [1, -1]:
						thisC = [startCol+i, startRow-i]
						if positionInArray([startCol+wordLength, startRow-wordLength]) and testForNoVal(thisC, wordGiven[i]):
							toAdd.append([thisC, wordGiven[i]])
							if i+1 == wordLength:
								thisIsOkay = True
					elif thisDirection == [-1, 0]:
						thisC = [startCol-i, startRow]
						if positionInArray([startCol-wordLength, startRow]) and testForNoVal(thisC, wordGiven[i]):
							toAdd.append([thisC, wordGiven[i]])
							if i+1 == wordLength:
								thisIsOkay = True
					elif thisDirection == [1, 0]:
						thisC = [startCol+i, startRow]
						if positionInArray([startCol+wordLength, startRow]) and testForNoVal(thisC, wordGiven[i]):
							toAdd.append([thisC, wordGiven[i]])
							if i+1 == wordLength:
								thisIsOkay = True
					elif thisDirection == [-1, 1]:
						thisC = [startCol-i, startRow+wordLength]
						if positionInArray([startCol-wordLength, startRow+wordLength]) and testForNoVal(thisC, wordGiven[i]):
							toAdd.append([thisC, wordGiven[i]])
							if i+1 == wordLength:
								thisIsOkay = True
					elif thisDirection == [0, 1]:
						thisC = [startCol, startRow+i]
						if positionInArray([startCol, startRow+wordLength]) and testForNoVal(thisC, wordGiven[i]):
							toAdd.append([thisC, wordGiven[i]])
							if i+1 == wordLength:
								thisIsOkay = True
					elif thisDirection == [1, 1]:
						thisC = [startCol+i, startRow+i]
						if positionInArray([startCol+wordLength, startRow+wordLength]) and testForNoVal(thisC, wordGiven[i]):
							toAdd.append([thisC, wordGiven[i]])
							if i+1 == wordLength:
								thisIsOkay = True
			else:
				break

		if attempts == 99:
			pass#print("Could not include " + str(letterList))

	#print("Successfully inputed: " + str(printWord))


for drawWords in range(len(words)):
	inputWord(words[drawWords].upper())

# Change all of the blank spots to random letters.
for r in range(ROWS):
	for c in range(COLS):
		if wsArray[r][c] == ' ':
			wsArray[r][c] = random.choice(alphebet)

print_array(wsArray)