import random
import find4

def checkwin(state, col, wc):
    z = len(state[col])-1
    print(z)
    print(col)
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
    testLose()
    forced = bouttaLoseVert()
    #print("here forced " + str(forced))
    if(forced != -1):
        print("here forced")
        return forced
    winMove = winningMove()
    #print("here won " + str(winMove))
    if (winMove != -1):
        print("here win")
        return winMove

    else:
        validMoves = random.randint(0, find4.x - 1)
        while len(find4.setup[validMoves]) > find4.x:
            validMoves = random.randint(0, find4.x - 1)
        return validMoves

def winningMove():
    for i in range(find4.x - 1):
        while len(find4.setup[i]) < find4.y:
            j = 0
            while j + 2 < len(find4.setup[i]) and j < (find4.x - 3):
                if find4.setup[i][j] == find4.setup[i][j + 1] and find4.setup[i][j + 1] == find4.setup[i][j + 2] and \
                        find4.setup[i][j] == -1:
                    return i
                else:
                    j += 1
            break
    return -1

def testLose():
    goodMove = -1
    for i in range(find4.x):
        cBoard = gameState()
        cBoard[i].append(-1)
        if checkwin(cBoard, i, find4.wincon-1) == True:
            goodMove = i
            print("yawokehio")
        else:
            print("yawNokehio")
    return goodMove

def bouttaLoseVert():
    for i in range(find4.x):
        #print("here's i " + str(i))
        while len(find4.setup[i]) < find4.y:
            j = 0
            while j+2 < len(find4.setup[i]) and j < (find4.x-3):
                #print("I and J " + str(i) + str(j))
                if find4.setup[i][j] == find4.setup[i][j+1] and find4.setup[i][j+1] == find4.setup[i][j+2] and find4.setup[i][j] == 1:
                    if j+3 < len(find4.setup[i]):
                        break
                    else:
                        return i
                else:
                    j+=1
            break
    return -1

def findBestMove():
    return
