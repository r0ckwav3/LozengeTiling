import random

SIZE = 2
low_tiling = [[0 for j in range(SIZE)] for k in range(SIZE)]
high_tiling = [[SIZE for j in range(SIZE)] for k in range(SIZE)]


def randomMove():
    # since we might count coordinates with multiple 0s multiple times, we
    # handle them seperately.

    poscount = (3 * (SIZE**2)) - (3*SIZE) + 1
    dieroll = random.randint(1, poscount)
    if dieroll == 1:
        pos = [0, 0, 0]
    elif dieroll <= (SIZE-1)*3 + 1:
        poscoord = random.randint(0, 2)
        pos = []
        for i in range(3):
            if i == poscoord:
                pos.append(random.randint(1, SIZE-1))
            else:
                pos.append(0)
    else:
        zerocoord = random.randint(0, 2)
        pos = []
        for i in range(3):
            if i == zerocoord:
                pos.append(0)
            else:
                pos.append(random.randint(1, SIZE-1))

    pushpull = bool(random.getrandbits(1))
    return (pos, pushpull)


# given a move, return the coordinates of the pile it affects
# if the move is not legal, returns None
def trueMovePos(heights, move):
    temppos = move[0][:]  # make a copy
    while max(temppos) < SIZE:
        targetheight = tempppos[2]
        if move[1]:
            targetheight += 1
        currheight = heights[temppos[0]][temppos[1]]
        if currheight == targetheight:
            return temppos[:2]
        elif currheight < targetheight:
            return None

        temppos = [e + 1 for e in temppos]

    return None


# destructive, modifies the configuration passed in
# does nothing if the move is illegal
def performMove(heights, move):
    movepos = trueMovePos(heights, move)
    if movepos is not None:
        if move[1]:
            heights[movepos] -= 1
        else:
            heights[movepos] += 1


# nondestructive, performs moves back to front
def performMoves(heights, move_list):
    newheights = heights[:]  # copy it over
    for i in range(len(move_list)-1, -1, -1):
        performMove(newheights, move_list[i])
    return newheights


def isIndependant(move_list):
    lt = performMoves(low_tiling, move_list)
    ht = performMoves(high_tiling, move_list)

    for x in range(SIZE):
        for y in range(SIZE):
            if lt[x][y] != ht[x][y]:
                return False

    return True


def randomConfig():
    move_list = []
    moves_per_step = 1
    while not isIndependant(move_list):
        for i in range(moves_per_step):
            move_list.append(randomMove())

        moves_per_step *= 2

    return performMoves(lt, move_list)
