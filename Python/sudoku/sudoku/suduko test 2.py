import numpy as np
import time

StartTime = 0
node = 0
searched = []
BadOut = np.full((9,9),-1,dtype=int)
Solution = BadOut
IdentSols = 0
Timeout = False

def ValidateSudoku(Sudoku):
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
    nums = 0
    for x in Sudoku:
        for y in x:
            if (y!=0):
                nums+=1
    if(nums<8):
        return False
    
    return True


def Duplicates(arr):
    for i in arr:
        if(i>0):
            if (len(np.delete(arr,np.where(arr!=i)))>1):
                return True
    return False

def RemDupes(Sols):
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

def sudoku_solver(sudoku):
    global searched
    global BadOut
    global StartTime
    global IdentSols
    global Solution
    Solution = BadOut
    StartTime = time.time()
    IdentSols = 0
    StartTime = time.time()
    searched = []
    if (not ValidateSudoku(sudoku)):
        return BadOut
    
    RawGrid = sudoku.copy()
    
    if (ValidateSudoku(RawGrid)):              
        tmp =  Solver(RawGrid.copy())
        #tmp = RemDupes(tmp)
        return (tmp)
    else:
        return BadOut
    



def ValidateMove(RawGrid, Move, Column, Row):
    for i in RawGrid:
        if i[Row] == Move:
            return False
            
    if (Move in RawGrid[Column]):
        return False
            
    
    SqColumn = (Column//3)*3
    SqRow = (Row//3)*3
    for i in range(0,3):
        if Move in RawGrid[SqColumn+i][SqRow:SqRow+3]:
            return False
    
    return True


def Solver(RawGrid):

    global searched
    global BadOut
    global node
    global StartTime
    global Solution
    global IdentSols
    global Timeout
    node+=1
    if (node % 150 == 0):
        if(time.time()-StartTime >=29.9):
            IdentSols = 10
            #Timeout = True
    if(IdentSols>=10):
        return Solution
    #print(node)
    sols = []
    swaps = False
    found = False
    for Column in range(0,9):
        for Row in range(0,9):
            if (RawGrid[Column][Row] == 0):
                found = True
                for i in range(1,10):
                    if(ValidateMove(RawGrid,i,Column,Row)):
                        tmp = RawGrid.copy()
                        tmp[Column][Row] = i
                        sols+=[Solver(tmp)]
                        swaps = True
                break
        if(found):
            break
    #print(sols)
    if(not swaps):
        
        tmp = True
        for Column in range(0,9):
            for Row in range(0,9):
                if (RawGrid[Column][Row] == 0):
                    tmp = False
                    break
            if(not tmp):
                break
        if(tmp):
            #print(RawGrid)
            if(np.array_equal(BadOut,Solution)):
                Solution = RawGrid
            elif(np.array_equal(RawGrid,Solution)):
                IdentSols+=1
            else:
                Solution = BadOut
                IdentSols = 10
                #print("double found")
                return BadOut
            return RawGrid
        else:
            return BadOut
    sols = RemDupes(sols)
    if(len(sols) == 0):
        #print("not enough sols")
        return BadOut
    elif( len(sols)>1):
        #print("too many sols")
        #print(sols)
        return BadOut
    else:
        return (sols[0])


puzzle = 11
sudokus = np.load("C:/Users/fitch/Desktop/Uni-Coding/Uni-Coding/Python/sudoku/sudoku/data/hard_puzzle.npy")
solutions = np.load("C:/Users/fitch/Desktop/Uni-Coding/Uni-Coding/Python/sudoku/sudoku/data/hard_solution.npy")
sol = solutions[puzzle].copy()
sudokutmp = sudokus[puzzle].copy()
print(sudokutmp)
print(sol)
tmp = sudoku_solver(sudokutmp)
print(tmp)
print(node)
print("")
print(Timeout)