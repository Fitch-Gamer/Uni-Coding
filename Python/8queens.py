import copy

tests = 0
fails = 0
nodes = 0

def SpaceFinder(SpacesLeftRaw,QueenNumRaw):
    SpacesLeft = copy.deepcopy(SpacesLeftRaw)
    QueenNum = copy.deepcopy(QueenNumRaw)
    global tests 
    global fails
    global nodes
    nodes +=1
    if QueenNum == 0:
        tests+=1
        return 1
    if SpacesLeft == []:
        tests +=1
        fails+=1
        return 0
    ScoreChange = 0
    for x in SpacesLeft:
        if x[0] == QueenNum:
            ScoreChange+=SpaceFinder(RemoveTaken(x,SpacesLeft),QueenNum-1)
    return ScoreChange
    
def RemoveTaken(QueenPosRaw,Board):
    BoardCopy=copy.deepcopy(Board)
    QueenPos = copy.deepcopy(QueenPosRaw)
    for square in Board:
        if square[0] == QueenPos[0] or square[1] == QueenPos[1] or square[0]-QueenPos[0] == square[1]-QueenPos[1] or square[0]-QueenPos[1] == square[1]-QueenPos[0]or square[1]-QueenPos[0] == square[0]-QueenPos[1] or QueenPos[0]-square[0] == QueenPos[1]-square[1]:
            BoardCopy.remove(square)
    
    return BoardCopy
    

ChessBoard = []
for x in range(1,9):
    for y  in range (1,9):
        ChessBoard.append((x,y))

print("successes: " + str(SpaceFinder(ChessBoard,8)))
print("fails: " + str(fails))
print("tests: " + str(tests))
print("nodes: " + str(nodes))