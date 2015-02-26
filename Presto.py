from random import *
from Graphics import *
import time
from Myro import *
import sys


win = Window("Prest-O!", 500, 500)
background = Rectangle((0,0), (500,500))
background.fill = Color("tan")
background.draw(win)
def newBoard():
    global win
    win = ""
    win = Window("Prest-O!", 500, 500)
    background = Rectangle((0,0), (500,500))
    background.fill = Color("tan")
    background.draw(win)
    newRound()

class Dot():

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        dot = Circle((self.x, self.y), 40)
        dot.fill = Color(self.color)
        dot.draw(win)



global colorBank
global choiceCounter
choiceCounter = 0
colorBank = ["Red", "Green", "Blue", "Yellow"]
def restoreColors():
    colorBank.extend( ["Red", "Green", "Blue", "Yellow"])
randomList = range(0, len(colorBank))


def colorChoice():
    if len(colorBank) == 0:
        return
    randIndex = randint(0,len(colorBank)-1)
    if colorBank[randIndex] in colorBank:
        dotColor = colorBank[randIndex]
        colorBank.remove(dotColor)
        #choiceCounter += 1
        return dotColor

global score
score = -1
global scoreboard
scoreboard = ""


## D1 = Dot(110,250, colorChoice())
## D1.draw()
## D2 = Dot(200, 250, colorChoice())
## D2.draw()
## D3 = Dot(290, 250, colorChoice())
## D3.draw()
## D4 = Dot(380, 250, colorChoice())
## D4.draw()
## restoreColors()


def shuffle():

    D1 = Dot(110,250, colorChoice())
    D1.draw()
    D2 = Dot(200, 250, colorChoice())
    D2.draw()
    D3 = Dot(290, 250, colorChoice())
    D3.draw()
    D4 = Dot(380, 250, colorChoice())
    D4.draw()
    restoreColors()

## for t in timer(60):
##     if int(t) % 5 == 0:
##         shuffle()

global prompt1
prompt1 = "{:s}"
global prompt2
prompt2 = "{:s}"
global promptCounter
promptCounter = 2

global gameover
gameover = ""
def gameoverWin():
    gameover = Text((250, 150), "Game Over!")
    gameover.fontSize = 20
    gameover.fill = Color("black")
    gameover.draw(win)

global presto
presto = ""


def prestoWin():

    presto = Text((250,150), "Prest-O!")
    presto.fontSize = 20
    presto.fill = Color("black")
    presto.draw(win)
    wait(1)

def randomColor():
    return colorBank[randint(0,len(colorBank)-1)]


def newRound():

    D1 = Dot(110,250, colorChoice())
    D1.draw()
    D2 = Dot(200, 250, colorChoice())
    D2.draw()
    D3 = Dot(290, 250, colorChoice())
    D3.draw()
    D4 = Dot(380, 250, colorChoice())
    D4.draw()
    exit = Rectangle((400,400),(450,450))
    exit.fill = Color("grey")
    exitPrompt = Text((425,425), "Exit")
    exitPrompt.fill = Color("Black")
    exit.draw(win)
    exitPrompt.draw(win)

    restoreColors()

    colorList = [randomColor(), randomColor()]

    text1 = Text((210,25), prompt1.format(colorList[0]))
    text1.fill = Color(randomColor())
    text1.draw(win)

    text2 = Text((290,25), prompt2.format(colorList[1]))
    text2.fill = Color(randomColor())
    text2.draw(win)

    wait(1)

    text1.undraw()
    text2.undraw()

    for targetColor in colorList:

        x = win.getMouse()[0]
        y = win.getMouse()[1]
        #print(x,y)

        if (x >= (D1.x - 40)) and (x <= (D1.x + 40)) and (y <= (D1.y + 40)) and (y >= (D1.y - 40)):
            if D1.color != targetColor:
                 gameoverWin()
                 text1.draw(win)
                 text2.draw(win)
                 return

        elif (x >= (D2.x - 40)) and (x <= (D2.x + 40)) and (y <= (D2.y + 40)) and (y >= (D2.y - 40)):
            if D2.color != targetColor:
                 gameoverWin()
                 text1.draw(win)
                 text2.draw(win)
                 return

        elif (x >= (D3.x - 40)) and (x <= (D3.x + 40)) and (y <= (D3.y + 40)) and (y >= (D3.y - 40)):
            if D3.color != targetColor:
                gameoverWin()
                text1.draw(win)
                text2.draw(win)
                return

        elif (x >= (D4.x - 40)) and (x <= (D4.x + 40)) and (y <= (D4.y + 40)) and (y >= (D4.y - 40)):
            if D4.color != targetColor:
                 gameoverWin()
                 text1.draw(win)
                 text2.draw(win)
                 return
        elif (x >= 400) and (x <= 450) and (y >= 400) and (y <= 450):
            quit = Text((250, 150), "Thanks for playing!")
            quit.fill = Color("Black")
            quit.draw(win)
            return
    prestoWin()
    newBoard()


newRound()
