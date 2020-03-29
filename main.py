import pygame
import time, sys, random
from wordsearchGenerator import returnWordPuzzle

# Initialize the program.
pygame.init()

# Define initial variable values.
SIZE = 15
MARGIN = 40
WIN_WIDTH = MARGIN + SIZE*40 + MARGIN + MARGIN*2
WIN_HEIGHT = MARGIN + SIZE*40 + 50
notRunning = False
linesToDraw = []

wsArray, wordKey, wordArray = returnWordPuzzle(SIZE)
print(wordKey)

# Set the Pygame display values.
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
backgroundColour = (255, 255, 255)
screen.fill(backgroundColour)

pygame.display.set_caption('Word Search')

start_time = time.time()
clock = pygame.time.Clock()

def drawText(labelText, xPos, yPos, thisType):
	sizeFnt = 25
	if thisType == "Input":
		thisColor = (52, 72, 97)#(117, 58, 14)
	elif thisType == "Back":
		thisColor = (0, 0, 0)
	elif thisType == "Red":
		thisColor = (132, 21, 0)#(245, 57, 12)
	elif thisType == "Timer":
		thisColor = (148, 163, 183)
	elif thisType == "Key":
		thisColor = (148, 163, 183)
		sizeFnt = 14
	font = pygame.font.Font('freesansbold.ttf', sizeFnt)	
	text = font.render(labelText, True, thisColor)
	textRect = text.get_rect()
	textRect.center = (xPos, yPos+3)
	return screen.blit(text, textRect)


def drawTimer():
	global timeElapsed, start_time, wordKey

	elapsed_time = time.time() - start_time
	#time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

	#pygame.draw.rect(screen, (200,150,70), (140, 20, 120, 120))
	drawText(str(time.strftime("%M:%S", time.gmtime(elapsed_time))), 60, WIN_HEIGHT - 37, "Timer")

	for let in range(len(wordArray)):
		drawText(wordArray[let], WIN_WIDTH - 70, MARGIN +(let*40), "Key")


def drawArray():
	yMarg = 0
	for line in range(SIZE+1):
		pygame.draw.line(screen, (0, 0, 0), (20 + (line*40), 20 + yMarg), (20 + (line*40), (MARGIN/2 + SIZE*40) + yMarg))
		pygame.draw.line(screen, (0, 0, 0), (20, 20 + (line*40) + yMarg), ((MARGIN/2 + SIZE*40), 20 + (line*40) + yMarg))

	drawLines()

	for row in range(SIZE):
		for col in range(SIZE):
			drawText(str(wsArray[row][col]), col*40 + MARGIN,row*40 + MARGIN + yMarg, "Back")
	

def drawLines():
	lineColor = (119, 189, 255)
	lineSize = 10
	mouseX, mouseY = pygame.mouse.get_pos()

	howManyLines = 0
	if len(linesToDraw)%2 == 0:
		howManyLines = len(linesToDraw)
	else:
		howManyLines = len(linesToDraw)-1

	for l in range(0, howManyLines, 2):
		if len(linesToDraw) > 1:
			x1, x2 = linesToDraw[l][0], linesToDraw[l+1][0]
			y1, y2 = linesToDraw[l][1], linesToDraw[l+1][1]
			pygame.draw.line(screen, lineColor, (x1, y1), (x2, y2), lineSize)
		else:
			break


	# if the length is even, draw it to mouseX
	if len(linesToDraw)%2 != 0:
		# pygame.draw.circle(screen, lineColor, (linesToDraw[len(linesToDraw)-1][0], linesToDraw[len(linesToDraw)-1][1]), 10, 1)
		# pygame.draw.circle(screen, lineColor, (mouseX, mouseY), 15, 1)
		pygame.draw.line(screen, lineColor, (linesToDraw[len(linesToDraw)-1][0], linesToDraw[len(linesToDraw)-1][1]), (mouseX, mouseY), lineSize)


def restartGame():
	global notRunning
	global wsArray
	global wordKey
	global start_time
	global SIZE

	notRunning = False
	start_time = time.time()

	wsArray, wordKey, wordArray = returnWordPuzzle(SIZE)

	updateDisplay()


# Main loop to continuously draw objects and process user input.
def updateDisplay():
	timeTracker = 0
	global notRunning, linesToDraw

	while not notRunning:
		mouseX, mouseY = pygame.mouse.get_pos()
		screen.fill(backgroundColour)

		for event in pygame.event.get():
			keyPressed = pygame.key.get_pressed()

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					sys.exit()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_g:
					returnWordPuzzle()
				elif event.key == pygame.K_z and keyPressed[pygame.K_LSHIFT]:
					if len(linesToDraw)%2 == 0 and len(linesToDraw) > 1:
						linesToDraw.pop(len(linesToDraw)-1)
						linesToDraw.pop(len(linesToDraw)-1)

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				linesToDraw.append([mouseX, mouseY])

			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				linesToDraw.append([mouseX, mouseY])
				
		
		drawArray()
		drawTimer()
	
		pygame.display.update()
		clock.tick(60)

	finishTime = time.time() - start_time

	#Stop processing coverField, wait for user to restart the game.
	while notRunning: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					restartGame() # HERE, reset startime variable
			
		screen.fill(backgroundColour)

		drawArray()
		thisRectW = 280
		pygame.draw.rect(screen, (239, 255, 234), (WIN_WIDTH/2 - thisRectW/2, (WIN_HEIGHT - 50)/2 - 30/2, thisRectW, 30))
		drawText("Press space to restart.", WIN_WIDTH/2, (WIN_HEIGHT - 50)/2, "Back")
		drawText(("Completed in: " + str(time.strftime("%M:%S", time.gmtime(finishTime)))), WIN_WIDTH/2, WIN_HEIGHT - 37, "Timer")

		pygame.display.flip()

		clock.tick(60)

updateDisplay()