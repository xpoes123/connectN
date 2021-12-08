import con4
import random
import math
import moveEval

'''To-do list
Currently move randomizer gets rid of the index if a move is illegal. IE if a row is filled, it will not take this into 
account. Please implement this

'''

#AI Turn
turn = -1

def checkwin(state, col, wc):
    z = len(state[col])-1
    ver = state[col][z]
    dir = [0,0,0]
    for h in [-1,1]:
        for v in range(-1,2):
            looking = True
            index = 1
            while looking and (0 <= col+index*h < con4.x) and (0 <= z+index*v < len(state[col+index*h])):
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

def checkDiag(state, col, wc):
    z = len(state[col])-1
    ver = state[col][z]
    dir = [0,0,0]
    for h in [-1,1]:
        for v in [-1,1]:
            looking = True
            index = 1
            while looking and (0 <= col+index*h < con4.x) and (0 <= z+index*v < len(state[col+index*h])):
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
    for i in range(con4.x):
        cBoard.append(list())
    for i in range(con4.x):
        for j in range(len(con4.setup[i])):
            cBoard[i].append(con4.setup[i][j])
    return cBoard

def pGameState(pgamer):
    cBoard = list()
    for i in range(con4.x):
        cBoard.append(list())
    for i in range(con4.x):
        for j in range(len(pgamer[i])):
            cBoard[i].append(pgamer[i][j])
    return cBoard

def isValid(col):
    cBoard = gameState()
    if len(cBoard[col]) < (con4.y-1):
        return True
    else:
        return False

def nextOpenRow(gameState, col):
    for r in range(con4.y-1):
        if gameState[r][col] == 0:
            return r

def drop(gameState, col, piece):
    return gameState[col].append(piece)

def getValidLoc():
    validLoc = []
    cBoard = gameState()
    for i in range(con4.x):
        if isValid(i):
            validLoc.append(i)
    return validLoc


def lose(curGameState):
    for i in range(con4.x):
        tempcBoard = pGameState(curGameState)
        tempcBoard[i].append(-1*turn)
        print(tempcBoard)
        if checkwin(tempcBoard, i, con4.wincon) == True:
            goodMove = i
            print(goodMove)
            return goodMove
    return -1

def lose2(curGameState):
    for i in range(con4.x):
        tempcBoard = pGameState(curGameState)
        tempcBoard[i].append(-1*turn)
        print(tempcBoard)
        if checkwin(tempcBoard, i, con4.wincon-1) == True:
            goodMove = i
            print(goodMove)
            return goodMove
    return -1

def lose3(curGameState):
    for i in range(con4.x):
        tempcBoard = pGameState(curGameState)
        tempcBoard[i].append(-1*turn)
        print(tempcBoard)
        if checkwin(tempcBoard, i, con4.wincon-2) == True:
            goodMove = i
            return goodMove
    return -1

def win(gameState, i):
    if checkwin(gameState, i, con4.wincon) == True:
        goodMove = i
        return goodMove
    return -1

def win2(gameState, i):
    if checkwin(gameState, i, con4.wincon-1) == True:
        goodMove = i
        return goodMove
    return -1

def win3(gameState, i):
    if checkwin(gameState, i, con4.wincon-2) == True:
        goodMove = i
        return goodMove
    return -1

def score(cGameState, i):
    score = 1
    x1 = win(cGameState, i)
    x2 = win2(cGameState, i)
    x3 = win3(cGameState, i)
    y1 = lose(cGameState)
    y2 = lose2(cGameState)
    y3 = lose3(cGameState)
    if x1 != -1:
        score += 1000
        print(str(score) + " :score")
    if x2 != -1:
        score += 50
        if (x2 == math.floor(con4.x / 2)):
            score += 20
        elif (x2 == math.floor(con4.x / 2) + 1 or x1 == math.floor(con4.x / 2) - 1):
            score += 10
        print(str(score) + " :score")
    if x3 != -1:
        score += 20
        if (x3 == math.floor(con4.x / 2)):
            score += 20
        elif (x3 == math.floor(con4.x / 2) + 1 or x1 == math.floor(con4.x / 2) - 1):
            score += 10
        print(str(score) + " :score")
    if y1 == -1:
        score += 900
        print(str(score) + " : don't lose score")
    if y2 == -1:
        score += 50
        if (y2 == math.floor(con4.x / 2)):
            score += 20
        elif (y2 == math.floor(con4.x / 2) + 1 or x1 == math.floor(con4.x / 2) - 1):
            score += 10
        print(str(score) + " :score")
    if y3 == -1:
        score += 20
        if (y3 == math.floor(con4.x / 2)):
            score += 20
        elif (y3 == math.floor(con4.x / 2) + 1 or x1 == math.floor(con4.x / 2) - 1):
            score += 10
        print(str(score) + " :score")

    return score

def bestMove():
    bestScore = -1000
    scoreList = list()
    cBoard = gameState()
    validLoc = getValidLoc()
    bestCol = list()
    for i in validLoc:
        cBoard = gameState()
        cBoard[i].append(turn)
        score2 = score(cBoard, i)
        scoreList.append(score2)
        print(str(score2) + " :score")
        print(str(bestScore) + " :bestscore")
        if score2 >= bestScore:
            print("here")
            bestScore = score2
    maxList = list()
    print(str(scoreList) + " score List")
    for i in range(len(scoreList)):
        if max(scoreList) <= scoreList[i]:
            maxList.append(i)
    print(str(maxList) + " best Moves")
    move = random.choice(maxList)
    return move

def winMove(turn):
    validLoc = getValidLoc()
    for i in validLoc:
        cBoard = gameState()
        cBoard[i].append(turn)
        if checkwin(cBoard, i, con4.wincon) == True:
            return validLoc[i]
