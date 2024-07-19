import sys
import itertools
import copy

args = [] # 0: InputFile, 1:OutputFile, 2:CodeLength (5 by default), 3:MaximumGuesses (12 by default), 4:AvailableColour (list of possible colours) (default is ["Red","Blue","Yellow","Green","Orange"])
Input = []
Output = []
CodeLength = 5
MaxGuesses = 12
Colours = []
Guesses = []
PlayerType = ""
Code = []
Searched = []
ComputerOutLine = []

def ArguementFormatter(): # formats the arguements into something easier to process
    global args
    global Input
    global Output
    global Colours
    global CodeLength
    global MaxGuesses

    args.pop(0)
    ArgsLen = len(args)
    if(ArgsLen<2):
        sys.exit(1)

    try: # validating and formatting the input file
        tmp = open(args[0], "r")
        for x in tmp:
            Input+=[x]
        tmp.close()
        InLen = len(Input)
        if(InLen==0):
            Out = open(args[1], "w")
            Out.write("No or ill-formed code provided")
            Out.close()
            raise Exception()
       
        if(InLen==1):
            Out = open(args[1], "w")
            Out.write("No or ill-formed player provided")
            Out.close()
            raise Exception()
        
    except:
        sys.exit(2)
    
    
    if(ArgsLen>2): # fomatting possible inputs
        try:
            CodeLength = int(args[2])
        except:
            Colours +=[args[2]]
    if(ArgsLen>3):
        try:
            MaxGuesses= int(args[3])
        except:
            Colours +=[args[3]]
    if(ArgsLen>4):
        for i in range(4,ArgsLen):
            Colours+=[args[i]]
    
    if(len(Colours) == 0):
        Colours = ["red","blue","yellow","green","orange"]

def ValidateInput(): # validates input and exits where appropiate
    global Input
    global Guesses
    global PlayerType
    global CodeLength
    global Code
    
    if((Input[0][:5]).lower() != "code "):
        Out = open(args[1], "w")
        Out.write("No or ill-formed code provided")
        Out.close()
        sys.exit(4)
    else:
        Code = (Input[0][5:]).split()
        if(len(Code)!=CodeLength):
            Out = Out = open(args[1], "w")
            Out.write("No or ill-formed code provided")
            Out.close()
            sys.exit(4)

    if((Input[1][:7]).lower() == "player " and ((Input[1][7:]).lower().strip() == "human" or (Input[1][7:]).lower().strip() == "computer")):
        PlayerType = (Input[1][7:]).lower().strip()
    else:
        Out = open(args[1], "w")
        Out.write("No or ill-formed player provided")
        Out.close()
        sys.exit(5)
    if(PlayerType == "human"):
        for i in range(2,len(Input)):
            Guesses+=[Input[i].split()]
        





        

def GamePlay(): # human gameplay
    global Input
    global Output
    global CodeLength
    global MaxGuesses
    global Colours
    global Guesses
    global PlayerType
    global Code
    Won = False
    i = 1
    BreakVar = False
    

    for Guess in Guesses:
        BreakVar = False
        if(len(Guess) == CodeLength):
            Blacks = 0
            Whites = 0
            j = 0
            tmp = Code.copy()
            for Colour in Guess:
                if(not (Colour in Colours)):
                   BreakVar = True
                   break
                if (tmp[j]==Colour):
                    tmp[j] = ""
                    Blacks+=1
                    Guess[j] = " "
                j+=1
            for Colour in Guess:
                j = 0
                for p in tmp:
                    if(p == Colour):
                        tmp[j] = ""
                        Whites+=1
                    j+=1
                
            if(not BreakVar):    
                Out = open(args[1], "a")
                Out.write("Guess " + str(i) + ": " + "black " * Blacks + "white " * Whites + "\n")
                Out.close()
                if(Blacks == CodeLength):
                    Out = open(args[1], "a")
                    Out.write("You won in " + str(i) + " guesses. Congratulations!\n")
                    Won = True
                    if(i != (len(Input)-2)):
                        Out.write("The game was completed. Further lines were ignored.\n")
                    Out.close()
                    BreakVar = True
                    break
            else:
                Out = open(args[1], "a")
                Out.write("Guess " + str(i) + ": Ill-formed guess provided\n")
                Out.close()
                
        else:
            Out = open(args[1], "a")
            Out.write("Guess " + str(i) + ": Ill-formed guess provided\n")
            Out.close()
        
        if(i>=MaxGuesses):
            Out = open(args[1], "a")
            Out.write("You can only have " + str(MaxGuesses) + " guesses.\n")
            Out.close()
            break

        i+=1
    if(not Won):
        Out = open(args[1], "a")
        Out.write("You lost. Please try again.")
        Out.close()


        
# Duran, N., 2019. Mastermind-Five-Guess-Algorithm [Online]. Availavle from: https://github.com/NathanDuran/Mastermind-Five-Guess-Algorithm

def GenPermutations(Elements,Length): # generating permutations for the above algorithm
    if(Length ==1):
        out = []
        for j in Elements:
            out+=[[j]]
    else:
        out = []
        tmp = GenPermutations(Elements,Length-1)
        for e in Elements:
            for i in tmp:
                out.append(i+[e])
    return out
            

def GetResult(Guess,Code): # result of a given guess with a given code
    global Colours

    Blacks = 0
    Whites = 0
    j = 0
    tmpGuess = list(copy.copy(Guess))
    tmp = list(copy.copy(Code))
    for Colour in tmpGuess:
        if (tmp[j]==Colour):
            tmp[j] = ""
            Blacks+=1
            tmpGuess[j] = "!"
        j+=1
    for Colour in tmpGuess:
        j = 0
        for p in tmp:
            if(p == Colour):
                tmp[j] = ""
                tmpGuess[j] = "!"
                Whites+=1
            j+=1
    return (Blacks,Whites)



def ComputateSol(CurPos,Guess,id): # computer guessing Ai
    global Input
    global Output
    global CodeLength
    global MaxGuesses
    global Colours
    global Guesses
    global PlayerType
    global Code
    global ComputerOutLine

    GuessResult = GetResult(Guess,Code)
    ComputerOutLine +=[" ".join(Guess) + "\n"]
    if(GuessResult[0]==CodeLength):
        tmp = open("computerGame.txt", "w")
        tmp.writelines(ComputerOutLine)
        Input = ComputerOutLine
        ValidateInput()
        GamePlay()

    else:
        if (id == 0):
            for Pos in (CurPos.copy()):
                if (GetResult(Guess,Pos) != GuessResult):
                    CurPos.remove(Pos)
            ComputateSol(CurPos,CurPos[0],0)
        else:
            tmp = copy.copy(CurPos) #added to deal with the first recursion of code which uses an iterator rather than a list
            CurPos = []
            for Pos in (tmp):
                if (GetResult(Guess,Pos) == GuessResult):
                    CurPos.append(Pos)
            print("next guess")
            ComputateSol(CurPos,CurPos[0],0)

    

args = sys.argv
ArguementFormatter()
ValidateInput()

if (PlayerType == "human"):
    GamePlay()
else:
    ComputerOutLine+=[Input[0]]
    ComputerOutLine+=["player human\n"]
    try:
        tmp = itertools.product(Colours,repeat=CodeLength)
    except:
        sys.exit(9) # using 9 for out of memory exception
    FstGuess = []
    if (len(Colours)>1): #ideally should produce an ideal first guess
        for i in range(0,CodeLength//2):
            FstGuess.append(Colours[0])
        LenAdd = CodeLength % 2

        for i in range(0,CodeLength//2 + LenAdd):
            FstGuess.append(Colours[1])
    else:
         for i in range(0,CodeLength):
            FstGuess.append(Colours[0]) 

    ComputateSol(tmp,FstGuess,1) # using an iterator for the first guess as a list for larger code length and code possibilites can cause an out of memory exception
    sys.exit(0)


