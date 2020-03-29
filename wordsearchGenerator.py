import random
# Started on 3/26/2020 6:36 PM, finished on 3/26/2020 8:47 PM.

# THE CODE IS CURRENTLY FUNCTIONAL AND MESSY, NOT OPTIMIZED YET!

# CHANGE THESE ---------------
 
words = ['Ackee','Apple','Apricot','Avocado','Banana','Bilberry','Blackberry','Blackcurrant','Blacksapote','Blueberry','Boysenberry','Breadfruit','Buddha','Cactus-pear','Crab-apple','Currant','Cherry','Cherimoya','Chico-fruit','Cloudberry','Coconut','Cranberry','Damson','Date','Dragonfruit']
words = ['Venice','Rome','Paris','Porto','Milan','Barcelona','London','Vienna','Verona','Prague','Moscow','Madrid']
words = ['PSG','Inter','ACMilan','Juventus','RealMadrid','Barcelona','Liverpool','Napoli','Roma','Ajax','Chelsea','ManCity','Atletico']
#-----------------------------
random.shuffle(words)

alphebet1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphebet = []

for elem in words:
	for i in range(len(alphebet1)):
		if alphebet1[i] in elem and not alphebet1[i] in alphebet:
			alphebet.append(alphebet1[i])

if 'D' not in alphebet:
	alphebet.append('D')
if 'G' not in alphebet:
	alphebet.append('G')
if 'F' not in alphebet:
	alphebet.append('F')
if 'L' not in alphebet:
	alphebet.append('L')
if 'O' not in alphebet:
	alphebet.append('O')
if 'T' not in alphebet:
	alphebet.append('T')

wsArray = []
SIZE = 0
COLS, ROWS = SIZE, SIZE
wordArray = []

for rows in range(ROWS):
	thisRow = []

	for cols in range(COLS):
		thisRow.append(' ')

	wsArray.append(thisRow)


#alphebet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

wordKey = "Word Key"

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
	global wsArray, wordKey
	startRow = 0
	startCol = 0
	wordLength = len(wordGiven) # Not -1?
	directions = [[-1, -1],[0, -1],[1, -1],[-1, 0],[1, 0],[-1, 1],[0, 1],[1, 1]] # [c,r] - NW,N,NE W E SW,S,SE
	#random.shuffle(directions)

	# Change this back, if it is possble, set it to thisDirection and break----------------------
	for e in range(len(directions)-1):
		rChange = directions[e][1]
		cChange = directions[e][0]
		if not positionInArray([startCol+ (wordLength*cChange), startRow+ (wordLength*cChange)]):
			directions[e] = 0

	newList = list(filter(lambda x: (x != 0), directions))
	random.shuffle(newList)
	#thisDirection = newList[0]

	#-----------------------------------------------------------------------------------------

	thisIsOkay = False
	toAdd = []
	printWord = []
	letterArray = []

	for let in range(wordLength):
		letterArray.append(wordGiven[let])

	for attempts in range(20):
		thisDirection = random.choice(newList)
		# Loop through possible directions
		if not thisIsOkay:
			toAdd = []

		startRow = random.randrange(ROWS)
		startCol = random.randrange(COLS)
		
		if wordLength <= ROWS or wordLength <= COLS:
			if thisIsOkay and len(toAdd) == len(wordGiven) and letterList == letterArray:
					printWord = []
					for a in range(len(toAdd)):
						lilC = toAdd[a][0][0]
						lilR = toAdd[a][0][1]
						lilLetterToPlace = toAdd[a][1]
						wsArray[lilR][lilC] = lilLetterToPlace
						printWord.append(lilLetterToPlace)
					
					wordKey = wordKey + ", " + wordGiven
					wordArray.append(str(wordGiven))
					break
					break
				

			for i in range(wordLength):
				letterList = []
				for n in range(len(toAdd)):
					letterList.append(toAdd[n][1])

				if len(letterList) > len(wordGiven):
					letterList = []
					toAdd = []
					break

				elif len(letterList) <= len(wordGiven):
				
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
					# else:
					# 	continue
				# else:
				# 	continue

			if attempts == 499:
				pass#print("Could not include " + str(letterList))

	#print("Successfully inputed: " + str(printWord))


def returnWordPuzzle(size):
	global wordKey, wsArray, ROWS, COLS, wordArray

	wordKey = "Word Key"
	wordArray = []
	wsArray = []
	ROWS = size
	COLS = size

	for rows in range(ROWS):
		thisRow = []
		for cols in range(COLS):
			thisRow.append(' ')
		wsArray.append(thisRow)

	for drawWords in range(len(words)):
		inputWord(words[drawWords].upper())

	#Change all of the blank spots to random letters.
	for r in range(ROWS):
		for c in range(COLS):
			if wsArray[r][c] == ' ':
				wsArray[r][c] = random.choice(alphebet)

	return wsArray, wordKey, wordArray