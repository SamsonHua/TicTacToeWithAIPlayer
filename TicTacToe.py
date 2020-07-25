from tkinter import *
import sys
import time
import random

win = False
counter = 0
globalPick = 0
counterDetect1 = 0
counterDetect2 = 0
lastPlayerMove = 0
suggestedMove = 0
matrix = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
default = "-"
starterplayer = "Default"


def setLastPlayerMove(derp):    
    return None


def LastPlayerMove(yeet):
    global lastPlayerMove
    lastPlayerMove = yeet
    print(lastPlayerMove)

def runCornerAI():
    global suggestedMove
    global starterplayer
    print("STARTED YEET")
    print(starterplayer)
    cornercounter = 0

    if(starterplayer == "AI"):
        if(matrix[0] == "-"):
            cornercounter = cornercounter + 1
        if (matrix[2] == "-"):
            cornercounter = cornercounter + 1
        if (matrix[6] == "-"):
            cornercounter = cornercounter + 1
        if (matrix[8] == "-"):
            cornercounter = cornercounter + 1
        print("corner counter: " + str(cornercounter))
        if(cornercounter > 0 and runDiagonalInterceptAI() == False and  runHorizontalInterceptAI() == False and  runVerticalInterceptAI() == False):
            if(cornercounter == 4):
                randomlol = random.randrange(0, 4)

                if(randomlol==0):
                    suggestedMove = 0
                if(randomlol==1):
                    suggestedMove = 2
                if(randomlol==2):
                    suggestedMove = 6
                if(randomlol==3):
                    suggestedMove = 8
                return True
            print("YEET!")
            if (matrix[0] == "-"):
                suggestedMove = 0
                return True
            elif (matrix[2] == "-"):
                suggestedMove = 2
                return True
            elif (matrix[6] == "-"):
                suggestedMove = 6
                return True
            elif (matrix[8] == "-"):
                suggestedMove = 8
                return True
            else:
                print("Error nani?")

    return False

def runVerticalWinAI():
    global turn
    global default
    global globalPick
    global suggestedMove
    # checks row
    print("Checking for" + turn)
    if globalPick < 3:
        # firstRow
        print("first row")
        if ((matrix[globalPick + 3] == turn or matrix[globalPick + 6] == turn) and (
                matrix[globalPick + 3] == default or matrix[globalPick + 6] == default)):
            print("DETECTED1")
            if (matrix[globalPick + 3] == turn):
                suggestedMove = globalPick + 6
                return True
            else:
                suggestedMove = globalPick + 3
                return True

        # if(lastPlayerMove == 0 or lastPlayerMove == 3 or lastPlayerMove == 6):
        # print("first column")
        # (lastPlayerMove == 1 or lastPlayerMove == 4 or lastPlayerMove ==7):
        # print("second column")
        # else:
        # print("third column")

    elif globalPick < 6:
        # secondRow
        print("second row")

        if ((matrix[globalPick - 3] == turn or matrix[globalPick + 3] == turn) and (
                matrix[globalPick - 3] == default or matrix[globalPick + 3] == default)):
            print("DETECTED2")
            if (matrix[globalPick + 3] == turn):
                suggestedMove = globalPick - 3
                return True
            else:
                suggestedMove = globalPick + 3
                return True

    else:
        # lastRow
        print("lastRow")

        if ((matrix[globalPick - 3] == turn or matrix[globalPick - 6] == turn) and (
                matrix[globalPick - 3] == default or matrix[globalPick - 6] == default)):
            print("DETECTED3")
            if (matrix[globalPick - 3] == turn):
                suggestedMove = globalPick - 6
                return True
            else:
                suggestedMove = globalPick - 3
                return True

    return False

def runHorizontalWinAI():
    global turn
    global default
    global globalPick
    global suggestedMove
    # checks column
    print("Checking for" + turn)
    if globalPick == 0 or globalPick == 3 or globalPick == 6:
        # firstcolumn
        print("first column")
        if ((matrix[globalPick + 1] == turn or matrix[globalPick + 2] == turn) and (
                matrix[globalPick + 1] == default or matrix[globalPick + 2] == default)):
            print("DETECTED1")
            if (matrix[globalPick + 1] == turn):
                suggestedMove = globalPick + 2
                return True
            else:
                suggestedMove = globalPick + 1
                return True

        # if(lastPlayerMove == 0 or lastPlayerMove == 3 or lastPlayerMove == 6):
        # print("first column")
        # (lastPlayerMove == 1 or lastPlayerMove == 4 or lastPlayerMove ==7):
        # print("second column")
        # else:
        # print("third column")

    elif globalPick == 1 or globalPick == 4 or globalPick == 7:
        # secondRow
        print("second column")

        if ((matrix[globalPick - 1] == turn or matrix[globalPick + 1] == turn) and (
                matrix[globalPick - 1] == default or matrix[globalPick + 1] == default)):
            print("DETECTED2")
            if (matrix[globalPick - 1] == turn):
                suggestedMove = globalPick + 1
                return True
            else:
                suggestedMove = globalPick - 1
                return True

    else:
        # lastRow
        print("lastRow")

        if ((matrix[globalPick - 2] == turn or matrix[globalPick - 1] == turn) and (
                matrix[globalPick - 2] == default or matrix[globalPick - 1] == default)):
            print("DETECTED3")
            if (matrix[globalPick - 2] == turn):
                suggestedMove = globalPick - 1
                return True
            else:
                suggestedMove = globalPick - 2
                return True

    return False

def runDiagonalWinAI():
    global turn
    global default
    global globalPick
    global suggestedMove
    # checks column
    print("Checking for" + turn)
    if globalPick == 4:
        # firstcolumn
        print("Diagonal Potentially Detected")
        if ((matrix[globalPick + 4] == turn or matrix[globalPick - 4] == turn) and (
                matrix[globalPick + 4] == default or matrix[globalPick - 4] == default)):
            print("DETECTED1")
            if (matrix[globalPick + 4] == turn):
                suggestedMove = globalPick - 4
                return True
            else:
                suggestedMove = globalPick + 4
                return True
        elif ((matrix[globalPick + 2] == turn or matrix[globalPick - 2] == turn) and (
                matrix[globalPick + 2] == default or matrix[globalPick - 2] == default)):
            if (matrix[globalPick + 2] == turn):
                suggestedMove = globalPick - 2
                return True
            else:
                suggestedMove = globalPick + 2
                print("intercepted")
                return True
    elif globalPick == 0:
        print("testing")
        if ((matrix[4] == turn or matrix[8] == turn) and (
                matrix[4] == default or matrix[8] == default)):
            if(matrix[4]==turn):
                suggestedMove = 8
                return True
            else:
                suggestedMove = 4
                return True
    elif globalPick == 2:
        if ((matrix[4] == turn or matrix[6] == turn) and (
                matrix[4] == default or matrix[6] == default)):
            if(matrix[4]==turn):
                suggestedMove = 6
                return True
            else:
                suggestedMove = 4
                return True
    elif globalPick == 6:
        if ((matrix[4] == turn or matrix[2] == turn) and (
                matrix[4] == default or matrix[2] == default)):
            if(matrix[4]==turn):
                suggestedMove = 2
                return True
            else:
                suggestedMove = 4
                return True
    elif globalPick == 8:
        if ((matrix[4] == turn or matrix[0] == turn) and (
                matrix[4] == default or matrix[0] == default)):
            if(matrix[4]==turn):
                suggestedMove = 0
                return True
            else:
                suggestedMove = 4
                return True

    return False

def runVerticalInterceptAI():
    global turn
    global default
    global lastPlayerMove
    global suggestedMove
    # checks row

    if lastPlayerMove < 3:
        # firstRow
        print("first row")
        if ((matrix[lastPlayerMove + 3] == oppositeturn or matrix[lastPlayerMove + 6] == oppositeturn) and (
                matrix[lastPlayerMove + 3] == default or matrix[lastPlayerMove + 6] == default)):

            if (matrix[lastPlayerMove + 3] == oppositeturn):
                suggestedMove = lastPlayerMove + 6
                return True
            else:
                suggestedMove = lastPlayerMove + 3
                return True

        # if(lastPlayerMove == 0 or lastPlayerMove == 3 or lastPlayerMove == 6):
        # print("first column")
        # (lastPlayerMove == 1 or lastPlayerMove == 4 or lastPlayerMove ==7):
        # print("second column")
        # else:
        # print("third column")

    elif lastPlayerMove < 6:
        # secondRow
        print("second row")

        if ((matrix[lastPlayerMove - 3] == oppositeturn or matrix[lastPlayerMove + 3] == oppositeturn) and (
                matrix[lastPlayerMove - 3] == default or matrix[lastPlayerMove + 3] == default)):
            print("DETECTED2")
            if (matrix[lastPlayerMove + 3] == oppositeturn):
                suggestedMove = lastPlayerMove - 3
                return True
            else:
                suggestedMove = lastPlayerMove + 3
                return True

    else:
        # lastRow
        print("lastRow")

        if ((matrix[lastPlayerMove - 3] == oppositeturn or matrix[lastPlayerMove - 6] == oppositeturn) and (
                matrix[lastPlayerMove - 3] == default or matrix[lastPlayerMove - 6] == default)):
            print("DETECTED3")
            if (matrix[lastPlayerMove - 3] == oppositeturn):
                suggestedMove = lastPlayerMove - 6
                return True
            else:
                suggestedMove = lastPlayerMove - 3
                return True

    return False


def runHorizontalInterceptAI():
    global turn
    global default
    global lastPlayerMove
    global suggestedMove
    # checks column
    print("Checking for" + oppositeturn)
    if lastPlayerMove == 0 or lastPlayerMove == 3 or lastPlayerMove == 6:
        # firstcolumn
        print("first column")
        if ((matrix[lastPlayerMove + 1] == oppositeturn or matrix[lastPlayerMove + 2] == oppositeturn) and (
                matrix[lastPlayerMove + 1] == default or matrix[lastPlayerMove + 2] == default)):
            print("DETECTED1")
            if (matrix[lastPlayerMove + 1] == oppositeturn):
                suggestedMove = lastPlayerMove + 2
                return True
            else:
                suggestedMove = lastPlayerMove + 1
                return True

        # if(lastPlayerMove == 0 or lastPlayerMove == 3 or lastPlayerMove == 6):
        # print("first column")
        # (lastPlayerMove == 1 or lastPlayerMove == 4 or lastPlayerMove ==7):
        # print("second column")
        # else:
        # print("third column")

    elif lastPlayerMove == 1 or lastPlayerMove == 4 or lastPlayerMove == 7:
        # secondRow
        print("second column")

        if ((matrix[lastPlayerMove - 1] == oppositeturn or matrix[lastPlayerMove + 1] == oppositeturn) and (
                matrix[lastPlayerMove - 1] == default or matrix[lastPlayerMove + 1] == default)):
            print("DETECTED2")
            if (matrix[lastPlayerMove - 1] == oppositeturn):
                suggestedMove = lastPlayerMove + 1
                return True
            else:
                suggestedMove = lastPlayerMove - 1
                return True

    else:
        # lastRow
        print("lastRow")

        if ((matrix[lastPlayerMove - 2] == oppositeturn or matrix[lastPlayerMove - 1] == oppositeturn) and (
                matrix[lastPlayerMove - 2] == default or matrix[lastPlayerMove - 1] == default)):
            print("DETECTED3")
            if (matrix[lastPlayerMove - 2] == oppositeturn):
                suggestedMove = lastPlayerMove - 1
                return True
            else:
                suggestedMove = lastPlayerMove - 2
                return True

    return False


def runDiagonalInterceptAI():
    global turn
    global default
    global lastPlayerMove
    global suggestedMove
    # checks column
    print("Checking for" + oppositeturn)
    if lastPlayerMove == 4:
        # firstcolumn
        print("Diagonal Potentially Detected")
        if ((matrix[lastPlayerMove + 4] == oppositeturn or matrix[lastPlayerMove - 4] == oppositeturn) and (
                matrix[lastPlayerMove + 4] == default or matrix[lastPlayerMove - 4] == default)):
            print("DETECTED1")
            if (matrix[lastPlayerMove + 4] == oppositeturn):
                suggestedMove = lastPlayerMove - 4
                return True
            else:
                suggestedMove = lastPlayerMove + 4
                return True
        elif ((matrix[lastPlayerMove + 2] == oppositeturn or matrix[lastPlayerMove - 2] == oppositeturn) and (
                matrix[lastPlayerMove + 2] == default or matrix[lastPlayerMove - 2] == default)):
            if (matrix[lastPlayerMove + 2] == oppositeturn):
                suggestedMove = lastPlayerMove - 2
                return True
            else:
                suggestedMove = lastPlayerMove + 2
                print("intercepted")
                return True
    elif lastPlayerMove == 0:
        print("testing")
        if ((matrix[4] == oppositeturn or matrix[8] == oppositeturn) and (
                matrix[4] == default or matrix[8] == default)):
            if(matrix[4]==oppositeturn):
                suggestedMove = 8
                return True
            else:
                suggestedMove = 4
                return True
    elif lastPlayerMove == 2:
        if ((matrix[4] == oppositeturn or matrix[6] == oppositeturn) and (
                matrix[4] == default or matrix[6] == default)):
            if(matrix[4]==oppositeturn):
                suggestedMove = 6
                return True
            else:
                suggestedMove = 4
                return True
    elif lastPlayerMove == 6:
        if ((matrix[4] == oppositeturn or matrix[2] == oppositeturn) and (
                matrix[4] == default or matrix[2] == default)):
            if(matrix[4]==oppositeturn):
                suggestedMove = 2
                return True
            else:
                suggestedMove = 4
                return True
    elif lastPlayerMove == 8:
        if ((matrix[4] == oppositeturn or matrix[0] == oppositeturn) and (
                matrix[4] == default or matrix[0] == default)):
            if(matrix[4]==oppositeturn):
                suggestedMove = 0
                return True
            else:
                suggestedMove = 4
                return True

    return False


def delay(yeet):
    time.sleep(yeet)
    return None


def randomizePlayer():
    global globalPick
    global turn
    global starterplayer
    label.configure(text="     ")
    randomize()
    startingPlayer = random.randrange(0, 2)
    print(startingPlayer)
    if startingPlayer == 0:
        starterplayer = "AI"
        runAI()
        print("I ran lmao")
        label.configure(text="AI is first, AI picked " + str(globalPick + 1))


    else:
        print("I ran too for some reason")
        label.configure(text="You go first! You are " + turn)
        starterplayer = "Player"


def checkcounter():
    global counter
    global win
    print("counter: " + str(counter))
    if counter == 9:

        win = True
        label.config(text="Game has ended in a tie!")
    return None


def reset():
    global counter
    global win
    global matrix
    counter = 0
    win = False

    matrix = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    randomizePlayer()
    refresh()


def randomize():
    global turn
    global oppositeturn
    startingState = random.randrange(0, 2)

    if startingState == 0:
        turn = "X"
        oppositeturn = "O"
        print("It is X")
    else:
        turn = "O"
        oppositeturn = "X"
        print("It is O")


def checkAIwin():
    global counter
    global win
    if (matrix[0] == turn and matrix[1] == turn and matrix[2] == turn) or (
            matrix[3] == turn and matrix[4] == turn and matrix[5] == turn) or (
            matrix[6] == turn and matrix[7] == turn and matrix[8] == turn) or (
            matrix[0] == turn and matrix[3] == turn and matrix[6] == turn) or (
            matrix[1] == turn and matrix[4] == turn and matrix[7] == turn) or (
            matrix[2] == turn and matrix[5] == turn and matrix[8] == turn) or (
            matrix[0] == turn and matrix[4] == turn and matrix[8] == turn) or (
            matrix[2] == turn and matrix[4] == turn and matrix[6] == turn):
        print("AI has won")
        label.configure(text="AI Wins, YOU SUCK!")
        win = True
        counter = 0
    return None


def checkPlayerWin():
    global win
    global counter
    if (matrix[0] == turn and matrix[1] == turn and matrix[2] == turn) or (
            matrix[3] == turn and matrix[4] == turn and matrix[5] == turn) or (
            matrix[6] == turn and matrix[7] == turn and matrix[8] == turn) or (
            matrix[0] == turn and matrix[3] == turn and matrix[6] == turn) or (
            matrix[1] == turn and matrix[4] == turn and matrix[7] == turn) or (
            matrix[2] == turn and matrix[5] == turn and matrix[8] == turn) or (
            matrix[0] == turn and matrix[4] == turn and matrix[8] == turn) or (
            matrix[2] == turn and matrix[4] == turn and matrix[6] == turn):
        label.configure(text="You win! Our AI Sucks")
        counter = 0
        print("player wins")
        win = True
    return None


def switchTurn():
    global turn
    global oppositeturn
    if win == False:

        if turn == "X":
            turn = "O"
            oppositeturn = "X"
        else:
            turn = "X"
            oppositeturn = "O"
        print("Value has been switched to " + turn)


def refresh():
    global win
    if win == False:
        button1.config(text=matrix[0])
        button2.config(text=matrix[1])
        button3.config(text=matrix[2])
        button4.config(text=matrix[3])
        button5.config(text=matrix[4])
        button6.config(text=matrix[5])
        button7.config(text=matrix[6])
        button8.config(text=matrix[7])
        button9.config(text=matrix[8])

    return None


def runAI():
    global globalPick
    global counter

    aiPick = random.randrange(0, 9)

    if win == False:

        if (runCornerAI() == True):
            print(suggestedMove)
            matrix[suggestedMove] = turn
            globalPick = suggestedMove
            label.configure(text="AI has picked spot " + str(suggestedMove + 1))
            counter = counter + 1
            refresh()
            checkAIwin()
            checkcounter()
            if win == False:
                switchTurn()
        elif(runVerticalWinAI() == True):
            print(suggestedMove)
            matrix[suggestedMove] = turn
            globalPick = suggestedMove
            label.configure(text="AI has picked spot " + str(suggestedMove + 1))
            counter = counter + 1
            refresh()
            checkAIwin()
            checkcounter()
            if win == False:
                switchTurn()
        elif (runHorizontalWinAI() == True):
            print(suggestedMove)
            matrix[suggestedMove] = turn
            globalPick = suggestedMove
            label.configure(text="AI has picked spot " + str(suggestedMove + 1))
            counter = counter + 1
            refresh()
            checkAIwin()
            checkcounter()
            if win == False:
                switchTurn()
        elif (runDiagonalWinAI() == True):
            print(suggestedMove)
            matrix[suggestedMove] = turn
            globalPick = suggestedMove
            label.configure(text="AI has picked spot " + str(suggestedMove + 1))
            counter = counter + 1
            refresh()
            checkAIwin()
            checkcounter()
            if win == False:
                switchTurn()
        elif (runVerticalInterceptAI() == True):
            print(suggestedMove)
            matrix[suggestedMove] = turn
            globalPick = suggestedMove
            label.configure(text="AI has picked spot " + str(suggestedMove + 1))
            counter = counter + 1
            refresh()
            checkAIwin()
            checkcounter()
            if win == False:
                switchTurn()
        elif (runHorizontalInterceptAI() == True):
            print(suggestedMove)
            matrix[suggestedMove] = turn
            globalPick = suggestedMove
            label.configure(text="AI has picked spot " + str(suggestedMove + 1))
            counter = counter + 1
            refresh()
            checkAIwin()
            checkcounter()
            if win == False:
                switchTurn()
        elif (runDiagonalInterceptAI() == True):
            print(suggestedMove)
            matrix[suggestedMove] = turn
            globalPick = suggestedMove
            label.configure(text="AI has picked spot " + str(suggestedMove + 1))
            counter = counter + 1
            refresh()
            checkAIwin()
            checkcounter()
            if win == False:
                switchTurn()
        else:
            if matrix[aiPick] == "-":
                matrix[aiPick] = turn
                globalPick = aiPick
                label.configure(text="AI has picked spot " + str(aiPick + 1))
                counter = counter + 1
                refresh()
                checkAIwin()
                checkcounter()
                if win == False:
                    switchTurn()
            else:
                runAI()


def confirmStatus(number):
    global counter
    if win == False:

        if matrix[number] == "-":
            matrix[number] = turn
            LastPlayerMove(number)
            refresh()
            checkPlayerWin()
            switchTurn()
            counter = counter + 1
            checkcounter()
            if win == False:
                print("boop")
                label.configure(text='[AI] Choosing spot....')
                runAI()

        else:
            print("")
            label.configure(text='Spot taken, choose again')


window = Tk()
window.geometry('370x400+100+100')
window.resizable(width=False, height=False)
window.title("Samson's Tic Tac Toe [Version 1.0.1]")
window.grid()
button1 = Button(window, text="-", height=5, width=10, font=('Ariel', '10'),
                 command=lambda: [confirmStatus(0), setLastPlayerMove(0)])
button1.grid(row=0, column=0)

button2 = Button(window, text="-", height=5, width=10, font=('Ariel', '10'),
                 command=lambda: [confirmStatus(1), setLastPlayerMove(1)])
button2.grid(row=0, column=1)

button3 = Button(window, text="-", height=5, width=10, font=('Ariel', '10'),
                 command=lambda: [confirmStatus(2), setLastPlayerMove(2)])
button3.grid(row=0, column=2)

button4 = Button(window, text="-", height=5, width=10, font=('Ariel', '10'),
                 command=lambda: [confirmStatus(3), setLastPlayerMove(3)])
button4.grid(row=1, column=0)

button5 = Button(window, text="-", height=5, width=10, font=('Ariel', '10'),
                 command=lambda: [confirmStatus(4), setLastPlayerMove(4)])
button5.grid(row=1, column=1)

button6 = Button(window, text="-", height=5, width=10, font=('Ariel', '10'),
                 command=lambda: [confirmStatus(5), setLastPlayerMove(5)])
button6.grid(row=1, column=2)

button7 = Button(window, text="-", height=5, width=10, font=('Ariel', '10'),
                 command=lambda: [confirmStatus(6), setLastPlayerMove(6)])
button7.grid(row=2, column=0)

button8 = Button(window, text="-", height=5, width=10, font=('Ariel', '10'),
                 command=lambda: [confirmStatus(7), setLastPlayerMove(7)])
button8.grid(row=2, column=1)

button9 = Button(window, text="-", height=5, width=10, font=('Ariel', '10'),
                 command=lambda: [confirmStatus(8), setLastPlayerMove(8)])
button9.grid(row=2, column=2)

resetbutton = Button(window, text="Reset", height=2, width=20, font=('Ariel', '7'), command=lambda: [reset()])
resetbutton.grid(row=70, column=1)

label = Label(window, text="                    ", font=('Ariel', '3'))
label.grid(row=50, column=1)
label = Label(window, text="                    ", font=('Ariel', '5'))
label.grid(row=60, column=1)

label = Label(window, text="Game booting up...", font=('Ariel', '10'))
#LOLEPICVICTORYROYALESAMSONLMAOOOOO
label.grid(row=55, column=1)
randomizePlayer()
window.mainloop()
