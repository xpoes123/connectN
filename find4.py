import davidEngine
import fish

#Inputs values for board dimensions and win conditions.
x = int(input("x: "))
y = int(input("y: "))
wincon = int(input("wincon: "))

#Creates board to play on.
setup = list()
for m in range(x):
    setup.append(list())

def checkwin(state, col, wc):
    z = len(state[col])-1
    print("Z" + str(z))
    ver = state[col][z]
    dir = [0,0,0]
    for h in [-1,1]:
        for v in range(-1,2):
            looking = True
            index = 1
            while looking and (0 <= col+index*h < x) and (0 <= z+index*v < len(state[col+index*h])):
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

playing = True
turn = -1
counter = 0
Human = False
while playing:
    turn *= -1
    Human = not Human
    print(str(turn) + "okeh")
    badchoice = True
    while badchoice:
        if Human == True:
            column = int(input("(Player Human" + str(turn) + ") Column: "))
        if Human == False:
            column = fish.findRandomMove()
            print(column)
        if len(setup[column]) < y:
            badchoice = False
            setup[column].append(turn)
            counter += 1
        else:
            if Human == False:
                continue
            else:
                print("That column is full, try again")
        print(setup)
        playing = not(checkwin(setup, column, wincon))
    if counter >= x * y:
        playing = False
if checkwin(setup, column, wincon):
    print("Game won by " + str(turn))
else: print("Game drawn")