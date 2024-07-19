import numpy as np
import copy
import time

StartTime = 0
searched = []
BadOut = np.full((9,9),-1,dtype=int) # defining this here so it saves time generating the value at the end
Solution = BadOut
MulSols = False

def RemDupes(Sols): # removes duplicate values in the array
    SolsCopy = Sols.copy()
    OutPut = []
    for i in SolsCopy:
        if(not np.array_equal(i,BadOut)):
            Pres = False
            for j in OutPut:
                if (np.array_equal(j,i)):
                    Pres = True
            if(not Pres):
                OutPut = OutPut + [i]
    return OutPut
        
            


def TriUnion(Arr1,Arr2,Arr3): # gets the values common accross the 3 arrays

    # runs through the 3 arrays to get common values so O(n^3) (assuming simialr length of each array)

    OutPut = []

    for x in Arr1:
        if(x>0):
            for y in Arr2:
                if (x==y): # no point waiting until the end to make this check, doing so here saves time
                    for z in Arr3:
                        if(x==z):
                            OutPut+=[x.copy()]
    return OutPut

def ValidateSudoku(Sudoku): # not necessarily the most optimised but as it only runs once on ititialisation, doesn't need to be
    Rows = Sudoku.copy()
    for i in Rows:
        if(Duplicates(i)):
            return False
    Columns = []
    for i in range(0,9):
        tmp = []
        for j in Sudoku.copy():
            tmp = tmp +[j[i]]
        Columns = Columns + [tmp]
    for i in Columns:
        if Duplicates(i):
            return False
    Squares = []
    j = 0
    tmp1 = []
    tmp2 = []
    tmp3 = []
    for i in Sudoku.copy():
        for k in range(0,3):
            tmp1 = tmp1 + [i[k]]
        
        for k in range(3,6):
            tmp2 = tmp2 + [i[k]]
        
        for k in range(6,9):
            tmp3 = tmp3 + [i[k]]
        
        j = j+1

        if (j == 3):
            j = 0
            Squares = Squares + [tmp1,tmp2,tmp3]
            tmp1 = []
            tmp2 = []
            tmp3 = []
    for i in Squares:
        if Duplicates(i):
            return False
    
    return True



def Duplicates(arr): # checks for duplicates in the array
    j = 0
    for i in arr:
        if(i>0):
            if (i in arr[j+1:len(arr)]):
                return True
        j+=1
    return False

def sudoku_solver(sudoku): # doing all the initialisation
    global searched
    global BadOut
    global StartTime
    global IdentSols
    global Solution

    IdentSols = 0
    StartTime = time.time()
    searched = []
    Solution = BadOut

    if (not ValidateSudoku(sudoku)):
        return BadOut
    
    RawGrid = sudoku.copy()
    LineTemp = np.arange(1,10,1)
    MissingInSquare = np.empty((9,9), dtype=int)
    MissingInColumn = np.empty((9,9), dtype=int)
    MissingInRow = np.empty((9,9), dtype=int)
    
    TotNum = 0

    for i in range (0,9):
        MissingInSquare[i] = LineTemp
        MissingInColumn[i] = LineTemp
        MissingInRow[i] = LineTemp



    for Column in range(0,9): # initialisation and definition of variables for the solver function
        for Row in range(0,9):
            CurNum = (RawGrid[Column][Row]).copy()
            if CurNum != -1:
                MissingInColumn[Column][MissingInColumn[Column] == CurNum] = -1
                MissingInRow[Row][MissingInRow[Row] == CurNum] = -1
                MissingInSquare[((Row//3) + (Column//3)*3)][MissingInSquare[((Row//3) + (Column//3)*3)] == CurNum] = -1

                TotNum +=1
    
    if(TotNum<17): # makes sure there is at least 17 numbers, required for a viable suduko as per McGuire(2014)
        return BadOut
    
    Swapped = True
    MulOpt = False
    MulOptChoices = []
    while(Swapped): # repeats until no swaps are made
        Swapped = False
        MulOpt = False
        MulOptChoices = []
        for Column in range(0,9): # this part of the function searches for all places where only 1 number can possibly be placed and as such is guaranteed to be placed there
            for Row in range(0,9):
                if RawGrid[Column][Row] == 0:

                    tmp = TriUnion(MissingInColumn[Column],MissingInRow[Row],MissingInSquare[((Row//3) + (Column//3)*3)]) # common numbers which haven't been placed in the row, column and square
                    length = len(tmp) # length is accessed more than once so this is quicker

                    if length == 1: # if only one number is possible
                        CurNum = tmp[0]
                        RawGrid[Column][Row] = CurNum

                        MissingInColumn[Column][MissingInColumn[Column] == CurNum] = -1 #adds the move to the missing locations
                        MissingInRow[Row][MissingInRow[Row] == CurNum] = -1
                        MissingInSquare[((Row//3) + (Column//3)*3)][MissingInSquare[((Row//3) + (Column//3)*3)] == CurNum] = -1

                        Swapped = True
                    elif length == 0:
                        return BadOut
                    else:
                        MulOptChoices.append((Column,Row,tmp)) # saves time repeating the union later
                        MulOpt = True
    
    
    if (MulOpt):
        return Solver(RawGrid.copy(),MissingInColumn.copy(),MissingInRow.copy(),MissingInSquare.copy(),MulOptChoices.copy())
    else:
        return(RawGrid)


def Solver(RawGrid,MissingInColumn,MissingInRow,MissingInSquare,MulOptChoices):

    global searched
    global BadOut
    global Solution
    global MulSols

    if(MulSols):
        return BadOut
    Swapped = True
    MulOpt = False
    tmp2 = MulOptChoices.copy()
    #print(tmp2)
    MulOptChoices = []
    while(Swapped): # repeats until no swaps are made
        Swapped = False
        MulOpt = False
        MulOptChoices = []
        for k in tmp2:
            #print("Here")
            #print(k)
            if RawGrid[k[0]][k[1]] == 0:
                tmp = TriUnion(MissingInColumn[k[0]],MissingInRow[k[1]],MissingInSquare[((k[1]//3) + (k[0]//3)*3)]) # common numbers which haven't been placed in the row, column and square
                length = len(tmp) # length is accessed more than once so this is quicker
                if length == 1: # i fonly one number is possible
                    CurNum = tmp[0]
                    RawGrid[k[0]][k[1]] = CurNum
                    MissingInColumn[k[0]][MissingInColumn[k[0]] == CurNum] = -1 #adds the move to the missing locations
                    MissingInRow[k[1]][MissingInRow[k[1]] == CurNum] = -1
                    MissingInSquare[((k[1]//3) + (k[0]//3)*3)][MissingInSquare[((k[1]//3) + (k[0]//3)*3)] == CurNum] = -1
                    Swapped = True
                elif length == 0:
                    return BadOut
                else:
                    MulOptChoices.append((k[0],k[1],tmp)) # saves time repeating the union later
                    MulOpt = True
    if (MulOpt): # if multiple moves for any are still possible
        #print("hit")
        
        MulOptChoices.sort(key=lambda x:len(x[2])) # puts the possible moves with the least possibilties to begin with to save number of nodes being checked
        sols = []
        ChosenMove = MulOptChoices[0] # saves accesing the longer array multiple times
        MulOptChoices.pop(0)
        for k in ChosenMove[2]:  # only acts on the first node in the list as it is a backtrack search and only acts on one location
            tmpGrid = (RawGrid.copy())
            tmpGrid[ChosenMove[0]][ChosenMove[1]] = k
            tmpColumn = MissingInColumn.copy()
            tmpRow = MissingInRow.copy()
            tmpSquares = MissingInSquare.copy()
            tmpColumn[ChosenMove[0]][tmpColumn[ChosenMove[0]] == k] = -1
            tmpRow[ChosenMove[1]][tmpRow[ChosenMove[1]] == k] = -1
            tmpSquares[((ChosenMove[1]//3) + (ChosenMove[0]//3)*3)][tmpSquares[((ChosenMove[1]//3) + (ChosenMove[0]//3)*3)] ==k ] = -1
            

            tmpOut = Solver(tmpGrid,tmpColumn,tmpRow,tmpSquares,MulOptChoices.copy())# using recursion to search the possible moves/nodes

            if(not np.array_equal(tmpOut,BadOut)): # if the solution is valid
                sols += [tmpOut]
                #print ("solution found")
                if(np.array_equal(Solution,BadOut)): # if no solution has already been found
                    Solution = tmpOut
                elif(not np.array_equal(Solution,tmpOut)): # if the solution found is different to a previous solution then theres an error
                    MulSols = True
                    return BadOut
            
        tmpsols = RemDupes(sols) # removes any duplicate solutions or bad solutions
        tmplen = len(tmpsols)
        if(tmplen==0): # if theres no or more solutions then there's an error
            return BadOut
        if(tmplen>1):
            MulSols = True
            return BadOut
        else:
            return sols[0]
    else:
        return RawGrid


puzzle = 11
sudokus = np.load("C:/Users/fitch/Desktop/Uni-Coding/Uni-Coding/Python/sudoku/sudoku/data/hard_puzzle.npy")
solutions = np.load("C:/Users/fitch/Desktop/Uni-Coding/Uni-Coding/Python/sudoku/sudoku/data/hard_solution.npy")
sol = solutions[puzzle].copy()
sudokutmp = sudokus[puzzle].copy()
print(sudokutmp)
print(sol)
tmp = sudoku_solver(sudokutmp)
print(tmp)
print("")
