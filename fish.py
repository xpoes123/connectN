import random
import find4

def checkwin(state, col, wc):
    z = len(state[col])-1
    ver = state[col][z]
    dir = [0,0,0]
    for h in [-1,1]:
        for v in range(-1,2):
            looking = True
            index = 1
            while looking and (0 <= col+index*h < find4.x) and (0 <= z+index*v < len(state[col+index*h])):
                if state[col+index*h][z+index*v] == ver:
                    dir[h*v] += 1
                    index += 1
                else: looking = False
    won = False
    if (len(state[col]) >= wc):
        stak = True
        for c in range(1,wc):
            if state[col][z-c] != ver:
                stak = False
        won = stak
    for d in dir:
        if d >= wc-1:
            won = True
    return won


def gameState():
    cBoard = list()
    for i in range(find4.x):
        cBoard.append(list())
    for i in range(find4.x):
        for j in range(len(find4.setup[i])):
            cBoard[i].append(find4.setup[i][j])
    return cBoard

def findRandomMove():
    forced = forceMove()
    #print("here forced " + str(forced))
    if(forced != -1):
        print("here forced")
        return forced
    else:

        validMoves = random.randint(0, find4.x - 1)
        while len(find4.setup[validMoves]) > find4.x:
            validMoves = random.randint(0, find4.x - 1)
        return validMoves

def firstMove():
    firstBoard = gameState()
    for i in range(find4.x):
        if len(firstBoard[i]) == 1:
            if i == 0:
                return 1
            elif i == 1:
                return 2
            elif i == 2:
                return 5
            elif i == 3:
                return 3
            elif i == 4:
                return 3
            elif i == 5:
                return 4
            elif i == 6:
                return 5

def forceMove():
    goodMove = -1
    turn = -1
    if find4.counter == 1:
        return firstMove()
    for i in range(find4.x):
        cBoard = gameState()
        cBoard[i].append(turn)
        if checkwin(cBoard, i, find4.wincon) == True:
            print("hi")
            goodMove = i
            return goodMove
    turn = 1
    for k in range(find4.x):
        cBoard = gameState()
        cBoard[k].append(turn)
        if checkwin(cBoard, k, find4.wincon) == True:
            print("hi2")
            goodMove = k
            return goodMove
    turn = -1
    for i in range(find4.x):
        cBoard = gameState()
        cBoard[i].append(turn)
        if checkwin(cBoard, i, find4.wincon-1) == True:
            goodMove = i
            return goodMove
    turn = 1
    for i in range(find4.x):
        cBoard = gameState()
        cBoard[i].append(turn)
        if checkwin(cBoard, i, find4.wincon-1) == True:
            print("hi")
            goodMove = i
            return goodMove
    return goodMove
