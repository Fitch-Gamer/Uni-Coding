import Data.Char

-- Note: I have reused code repeatedly under 'where' statements as I was unsure if adding additional functions by default was allowed
-- I have also used let statements do delcare a variable for the sole intent of repeating intensive functions when using the variable/function multiple times in a function
-- I would also refactor a lot of it to make it more efficent and add more detailed comments but I was struggling for time after exercise 5

------------------------- Merge sort

merge :: Ord a => [a] -> [a] -> [a]
merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
    | x <  y    = x : merge    xs (y:ys)
    | x == y    = x : merge    xs    ys
    | otherwise = y : merge (x:xs)   ys

msort :: Ord a => [a] -> [a]
msort []  = []
msort [x] = [x]
msort xs  = msort (take n xs) `merge` msort (drop n xs)
  where
    n = length xs `div` 2
    
------------------------- Game world types

type Character = String
type Party     = [Character]

type Node      = Int
type Location  = String
type Map       = [(Node,Node)]

data Game      = Over
               | Game Map Node Party [Party]
  deriving (Eq,Show)

type Event     = Game -> Game


testGame :: Node -> Game
testGame i = Game [(0,1)] i ["Russell"] [[],["Brouwer","Heyting"]]


------------------------- Assignment 1: The game world

connected :: Map -> Node -> [Node] -- returns connected nodes (forgot this exists later in the code)
connected [] _ = []
connected (m:ms) n
  | (fst m) == n = [(snd m)] ++ (connected ms n)
  | (snd m) == n = [(fst m)] ++ (connected ms n)
  | otherwise = (connected ms n)


connect :: Node -> Node -> Map -> Map -- connects two nodes and adds as an ordered list to the map
connect i j map
  | (inmap i j map) = map
  | otherwise = addorderednode (i,j) map
  where
    inmap:: Node -> Node -> Map -> Bool
    inmap _ _ [] = False
    inmap i j (x:xs)
      | (i,j) == x = True
      | (j,i) == x = True
      | otherwise = inmap i j xs
    
    addorderednode:: (Node,Node) -> Map -> Map -- adds the node into the list ordered
    addorderednode n [] = [n]
    addorderednode n (x:xs) 
      | (fst n) == (fst x) && (snd n) < (snd x) ||((fst n) < (fst x))  = n:x:xs
      | otherwise = x:(addorderednode n xs) 


disconnect :: Node -> Node -> Map -> Map -- disconnects two nodes
disconnect _ _ [] = []
disconnect  i j (x:xs)
  | (i,j) == x = xs
  | (j,i) == x = xs
  | otherwise =  x:(disconnect i j xs)

add :: Party -> Event -- adds to party
add p = addParty p
  where
    addParty :: Party -> Game -> Game
    addParty _ Over = Over
    addParty p (Game n m par parl) = (Game n m (msort(p++par)) parl)

addAt :: Node -> Party -> Event -- adds to party at location
addAt nd p = addParty p nd 0
  where
    addParty :: Party -> Node -> Int -> Game -> Game
    addParty _ _ _ Over = Over
    addParty p nd curnd (Game m n par (x:xs)) 
      | nd == curnd = (Game m n (par) ((msort (x++p)):xs))
      | otherwise = addAtLoc x (addParty p nd (curnd+1) (Game m n par (xs)))

    addAtLoc :: Party -> Game -> Game
    addAtLoc p (Game m n par (x:xs)) = (Game m n par (p:x:xs))

addHere :: Party -> Event -- adds to party here
addHere p = addinghere p
  where
    addinghere :: Party -> Game -> Game
    addinghere p (Game m n par (x:xs)) = addAt n p (Game m n par (x:xs))

remove :: Party -> Event -- removes from party
remove p = filcontains p
  where
    filcontains:: Party -> Game -> Game

    filcontains _ Over = Over

    filcontains [] (Game m n [] (x:xs)) = (Game m n [] (x:xs))

    filcontains [] (Game m n [] []) = (Game m n [] [])

    filcontains p (Game m n par []) = (Game m n (filter (contains p) par) [])

    filcontains p (Game m n par (x:xs)) = (Game m n (filter (contains p) par) (x:xs))

    contains :: Party -> Character -> Bool
    contains [] _ = True
    contains (x:xs) c 
      | c == x = False
      | otherwise = contains xs c

removeAt :: Node -> Party -> Event -- removes from party at location
removeAt n p = remParty p n 0
  where
    remParty :: Party -> Node -> Int -> Game -> Game
    remParty _ _ _ Over = Over
    remParty p nd curnd (Game m n par (x:xs)) 
      | nd == curnd = (Game m n (par) ((filter (contains p) (x)):xs))
      | otherwise = addAtLoc x (remParty p nd (curnd+1) (Game m n par (xs)))

    addAtLoc :: Party -> Game -> Game
    addAtLoc p (Game m n par (x:xs)) = (Game m n par (p:x:xs))
    
    contains :: Party -> Character -> Bool
    contains [] _ = True
    contains (x:xs) c 
      | c == x = False
      | otherwise = contains xs c

removeHere :: Party -> Event -- removes from party here
removeHere p = remhere p
  where
    remhere :: Party -> Game -> Game
    remhere p (Game m n par (x:xs)) = removeAt n p (Game m n par (x:xs))


------------------------- Assignment 2: Dialogues


data Dialogue = Action  String  Event
              | Branch  (Game -> Bool) Dialogue Dialogue
              | Choice  String  [( String , Dialogue )]

testDialogue :: Dialogue
testDialogue = Branch ( isAtZero )
  (Choice "Russell: Let's get our team together and head to Error." [])
  (Choice "Brouwer: How can I help you?"
    [ ("Could I get a haircut?", Choice "Brouwer: Of course." [])
    , ("Could I get a pint?",    Choice "Brouwer: Of course. Which would you like?"
      [ ("The Segmalt.",     Action "" id)
      , ("The Null Pinter.", Action "" id)]
      )
    , ("Will you join us on a dangerous adventure?", Action "Brouwer: Of course." (add ["Brouwer"] . removeHere ["Brouwer"]))
    ]
  )
 where
  isAtZero (Game _ n _ _) = n == 0


dialogue :: Game -> Dialogue -> IO Game

dialogue g (Action s e) = do
  putStrLn("")
  putStrLn(s)
  let temp = e g
  return (temp)
    
dialogue g (Branch f d1 d2) = if (f g) then (dialogue g d1) else (dialogue g d2)

dialogue g (Choice s []) = do
  putStrLn("")
  putStrLn(s)
  return g

dialogue g (Choice s (x:xs)) = do -- all the stuff to make the choice looik nice is here
  putStrLn("")
  putStrLn("")
  putStrLn("")
  putStrLn s
  putStrLn("")
  list (x:xs) 1
  putStrLn ""
  putStr ">> "
  line <- getLine
  putStrLn("")
  let test = foldr (&&) True (map isDigit line) && line /= ""
  let input = if test then (Just (read line :: Int)) else Nothing
  let tmpDialogue = if test then (getDialogue (extract input) (x:xs) 1) else Nothing
  
  if (check input) == False then do -- this is where the input is processed and below
    putStrLn("Sorry that is an invalid input, please try again")
    dialogue g (Choice s (x:xs))
    else if (extract input) == 0 then do
    return g
    else  dialogue g ((extract (tmpDialogue)))
    where

      check :: Maybe a -> Bool
      check (Nothing) = False
      check (Just _) = True

      extract :: Maybe a -> a
      extract (Just a) = a

      list :: [(String, Dialogue)] -> Int -> IO()

      list [] _ = return ()

      list (x:xs) i = do
        putStrLn ( (show i) ++ ". " ++ (fst x))
        list xs (i+1)
    
      getDialogue :: Int -> [(String,Dialogue)] -> Int -> Maybe Dialogue
      getDialogue _ [] _ = Nothing
      getDialogue  i (x:xs) j
        | i == j = Just (snd x)
        | otherwise = getDialogue i xs (j+1)
      

findDialogue :: Party -> Dialogue -- iterates through all dialogues to find dialogue
findDialogue p = search p theDialogues
  where
    search :: Party -> [(Party,Dialogue)] -> Dialogue
    search p [] = (Choice "There is nothing we can do." [])
    search p (x:xs)
      | fst x == p = snd x
      | otherwise = search p xs



------------------------- Assignment 3: The game loop

step :: Game -> IO Game -- makes the step look nice ot the user
step Over = return Over
step (Game m n p pAtLoc)= do
  putStrLn("")
  putStrLn("")
  putStrLn("")
  putStrLn ("You are in " ++ (getIter n 0 theDescriptions))
  let possibleLoc = (getPossibleLoc n m)
  if possibleLoc /=[] then do 
    putStrLn("")
    putStrLn ("You can travel to:") else putStr("")
  curnum <- numList possibleLoc 1
  let maxLocNum = (curnum-1)
  if p /= [] then do 
    putStrLn("")
    putStrLn ("With you are:") 
    else putStr("")
  curnum <- numList p curnum
  let maxParNum = (curnum-1)
  if (getIter n 0 pAtLoc) /= [] then do 
    putStrLn("")
    putStrLn ("You can see:") else putStr("")
  curnum <- numList (getIter n 0 pAtLoc) curnum
  let maxNum = (curnum-1)
  putStrLn("")
  putStrLn("What will you do?")
  putStrLn("")
  putStr(">> ")
  tmp <- getLine
  
  temp <- (processInput  (words (tmp)) (Game m n p pAtLoc) maxLocNum maxParNum maxNum)

  if temp == Over then return Over else return temp

  where    -- all the input is processed to the action to be done
    numList:: [String] -> Int -> IO Int
    numList [] i = return i
    numList (x:xs) i = do
      putStrLn ("   "++(show i) ++ ". " ++ x)
      (numList xs (i+1))

    getPossibleLoc:: Int -> Map -> [Location]
    getPossibleLoc _ [] = []
    getPossibleLoc i (x:xs)
      | fst x == i = (getIter (snd x) 0 theLocations):(getPossibleLoc i xs)
      | snd x == i = (getIter (fst x) 0 theLocations):(getPossibleLoc i xs)
      | otherwise = (getPossibleLoc i xs)

    getIter :: Int -> Int -> [a] -> a
    getIter i j (x:xs)
      | i == j = x
      | otherwise = getIter i (j+1) xs 

    getPos :: Eq a => a -> [a] -> Int -> Int
    getPos a (x:xs) j 
      | x == a = j
      | otherwise = (getPos a xs (j+1))

    getChars :: [String] -> [String] -> Int -> [String]
    getChars [] _ _ = []
    getChars (x:xs) (y:ys) z = (getIter ((read x :: Int)-z -1) 0 (y:ys) ):(getChars xs (y:ys) z)

    processInput:: [String] -> Game -> Int -> Int -> Int -> IO Game
    processInput _ Over _ _ _ = return Over
    processInput [] (Game m n p pAtLoc) maxLocNum maxParNum maxNum = do
        putStrLn ("Sorry that is not a valid input, valid inputs are 0 to return to exit or " ++ (if maxLocNum == 0 then "" else " 1 to " ++ show maxLocNum ++ " for locations or ")  ++ show (maxLocNum+1) ++ " to " ++ show maxNum ++ " or a combination of these (seperated by spaces) for character dialogue, please try again")
        step (Game m n p pAtLoc)
    processInput (x:xs) (Game m n p pAtLoc) maxLocNum maxParNum maxNum
      | foldr (&&) True (map ((foldr (&&) True).(map isDigit)) (x:xs)) == False = do
        putStrLn ("Sorry that is not a valid input, valid inputs are 0 to return to exit or " ++ (if maxLocNum == 0 then "" else " 1 to " ++ show maxLocNum ++ " for locations or ")  ++ show (maxLocNum+1) ++ " to " ++ show maxNum ++ " or a combination of these (seperated by spaces) for character dialogue, please try again")
        step (Game m n p pAtLoc)
      | (read x :: Int) == 0 = return Over
      | (read x :: Int) <= maxLocNum = do 
         let y = (getPossibleLoc n m)
         let z = (getIter ((read x :: Int)-1) 0 y)
         let k = (getPos z theLocations 0)
         let tmp = (Game m k p pAtLoc)
         return tmp
      | (read x :: Int) <= maxNum = dialogue (Game m n p pAtLoc) (findDialogue (msort (getChars (x:xs) (p ++ (getIter n 0 pAtLoc)) maxLocNum)))
      | (read x :: Int) > maxNum = do
        putStrLn ("Sorry that is not a valid input, valid inputs are 0 to return to exit or " ++ (if maxLocNum == 0 then "" else " 1 to " ++ show maxLocNum ++ " for locations or ")  ++ show (maxLocNum+1) ++ " to " ++ show maxNum ++ " or a combination of these (seperated by spaces) for character dialogue, please try again")
        step (Game m n p pAtLoc)
      | otherwise = do 
          return Over




game :: IO ()
game = do
  loop start
  putStrLn("Thanks for playing!") -- finishing note for the player
  where 
    loop:: Game -> IO Game -- loops through step until game is over
    loop Over = return Over
    loop g = do 
      tmp <- step g
      loop (tmp)

------------------------- Assignment 4: Safety upgrades


------------------------- Assignment 5: Solving the game

data Command  = Travel [Int] | Select Party | Talk [Int]
  deriving Show

type Solution = [Command]

talk ::Game -> Dialogue -> [(Game,[Int])] -- recursion to opbain every combination which goes to an action
talk g (Action _ e)= [((e g),[])] 
talk g (Branch f d1 d2) = if (f g) then talk g d1 else talk g d2
talk g (Choice s []) = []
talk g (Choice s (x:xs)) = processChoice g (Choice s (x:xs)) 1
  where
    processChoice:: Game -> Dialogue -> Int -> [(Game,[Int])]
    processChoice g (Choice _ []) i = []
    processChoice g (Choice s (x:xs)) i = (increment i (talk g (snd x))) ++ (processChoice g (Choice s xs) (i+1))

    increment:: Int -> [(Game,[Int])] -> [(Game, [Int])]
    increment _ [] = []
    increment i ((a,b):xs) = (a,(i:b)):(increment i xs)

select :: Game -> [Party] -- uses permutations to get all possible combinations
select (Game m n p pAtLoc) = map msort (permutations (p++(getIter n 0 pAtLoc))++ [[]])
  where
    getIter :: Int -> Int -> [a] -> a
    getIter i j (x:xs)
      | i == j = x
      | otherwise = getIter i (j+1) xs 
    
    permutations:: [a] -> [[a]]
    permutations [] = [[]]
    permutations [x] = [[x]] 
    permutations (x:xs) = [[x]]++(nestedAppend x (permutations xs))++(permutations xs)

    nestedAppend:: a -> [[a]] ->[[a]]
    nestedAppend _ [] = []
    nestedAppend a (x:xs) = (append a x):(nestedAppend a xs) 

    append:: a -> [a] -> [a]
    append x xs = x:xs

travel :: Map -> Node -> [(Node,[Int])] -- loops over dijkstras algorithm to get shortest rroute to each node
travel m n = shortestNodes m n 0 (maxIn m 0) [(n,[])] [] 
  where

    shortestNodes:: Map -> Node -> Int -> Int -> [(Node,[Int])] -> [Int] -> [(Node,[Int])]
    shortestNodes map startnod iter max (nodl:nodls) curlist = dijkstrasTo 0 (maxIn map 0) (dijkstras startnod map []) map

    dijkstrasTo :: Int -> Int -> (Int -> [Int]) -> Map -> [(Node, [Int])]
    dijkstrasTo cur end f m
      | cur == end = [(cur,(convertToIter (f cur) m))] 
      | otherwise = (cur,(convertToIter (f cur) m)) :(dijkstrasTo (cur+1) end f m)
    
    convertToIter:: [Node] -> Map ->[Node]
    convertToIter [] _ = []
    convertToIter (_:[]) _ = []
    convertToIter (x:n:xs) m = (getPos n (getPossibleLoc x m) 1):(convertToIter (n:xs) m)

    dijkstras::Node -> Map -> [Int] -> Node -> [Node]
    dijkstras curNode map explored end
      | removeFrom explored (getPossibleLoc curNode map) == [] = []
      | otherwise = do 
          let posloc = removeFrom explored (getPossibleLoc curNode map)
          if (contains end posloc) then [curNode,end]
          else do
            let search = dijkstrasLoop posloc [] map (curNode:explored) end 
            if (search == []) then [] 
              else curNode:search
      
    dijkstrasLoop:: [Node] -> [Node] -> Map -> [Node] -> Node -> [Node]
    dijkstrasLoop [] curSol _ _ _ = curSol
    dijkstrasLoop (x:xs) curSol map explored end = do
      let search = dijkstras x map explored end
      if search == [] then dijkstrasLoop xs curSol map explored end
      else if (length search) < (length curSol) || curSol == [] then dijkstrasLoop xs search map explored end
      else dijkstrasLoop xs curSol map explored end
        
    getPos :: Eq a => a -> [a] -> Int -> Int
    getPos a (x:xs) j 
      | x == a = j
      | otherwise = (getPos a xs (j+1))
      
    contains:: Eq a => a -> [a] -> Bool
    contains _ [] = False
    contains a (x:xs)
      | a == x = True
      | otherwise = contains a xs


    removeFrom:: Eq a => [a] -> [a] -> [a]
    removeFrom _ [] = []
    removeFrom [] b = b
    removeFrom (x:xs) from = removeFrom xs (remove x from)


    remove:: Eq a => a -> [a] ->[a]
    remove _ [] = []
    remove z (x:xs)
      | x == z = remove z xs
      | otherwise = x:(remove z xs)

    maxIn:: [(Node,Node)] -> Int -> Int
    maxIn [] n = n
    maxIn (x:xs) n
      | fst x > n && fst x > snd x = maxIn xs (fst x)
      | snd x > n && snd x > fst x = maxIn xs (snd x)
      | otherwise = maxIn xs n

    getPossibleLoc:: Int -> Map -> [Int]
    getPossibleLoc _ [] = []
    getPossibleLoc i (x:xs)
      | fst x == i = (snd x):(getPossibleLoc i xs)
      | snd x == i = (fst x):(getPossibleLoc i xs)
      | otherwise = (getPossibleLoc i xs)

allSteps :: Game -> [(Solution,Game)] -- loops 3 times over the game to try all possible steps
allSteps g = everyLoc g 0
  where

    maxIn:: [(Node,Node)] -> Int -> Int
    maxIn [] n = n
    maxIn (x:xs) n
      | fst x > n && fst x > snd x = maxIn xs (fst x)
      | snd x > n && snd x > fst x = maxIn xs (snd x)
      | otherwise = maxIn xs n

    appendToFst:: [([a],b)] -> a -> [([a],b)]
    appendToFst [] _ = []
    appendToFst ((a,b):xs) c = ((c:a),b):(appendToFst xs c) 

    everyLoc:: Game -> Int ->[(Solution,Game)]
    everyLoc (Game m n p pAtLoc) i
      | i >= maxIn m 0 = []
      | otherwise = do 
        let tmp = (convertToIter (dijkstras n m [] i) m)
        if tmp /= [] || n ==i 
        then (appendToFst(everyDia (Game m i p pAtLoc) (select (Game m i p pAtLoc))) (Travel tmp)) ++ everyLoc (Game m n p pAtLoc) (i+1)
        else everyLoc (Game m n p pAtLoc) (i+1)

    everyDia:: Game -> [Party] -> [(Solution,Game)]
    everyDia _ [] = []
    everyDia (Game (m:ms) n par pAtLoc) (p:ps) = do
      let tmp = findDialogue p
      if (extractChoice tmp) == "There is nothing we can do." 
        then everyDia (Game (m:ms) n par pAtLoc) ps 
        else (appendToFst (everyTalk (talk (Game (m:ms) n par pAtLoc) tmp)) (Select p)) ++ (everyDia (Game (m:ms) n par pAtLoc) ps )

    extractChoice:: Dialogue -> String
    extractChoice (Choice s _) = s
    extractChoice _ = ""

    everyTalk:: [(Game,[Int])] -> [(Solution,Game)]
    everyTalk [] = []
    everyTalk ((a,b):xs) = ([(Talk b)],a):(everyTalk xs)
    


    convertToIter:: [Node] -> Map ->[Node]
    convertToIter [] _ = []
    convertToIter (_:[]) _ = []
    convertToIter (x:n:xs) m = (getPos n (getPossibleLoc x m) 1):(convertToIter (n:xs) m)

    dijkstras::Node -> Map -> [Int] -> Node -> [Node]
    dijkstras curNode map explored end
      | removeFrom explored (getPossibleLoc curNode map) == [] = []
      | otherwise = do 
          let posloc = removeFrom explored (getPossibleLoc curNode map)
          if (contains end posloc) then [curNode,end]
          else do
            let search = dijkstrasLoop posloc [] map (curNode:explored) end 
            if (search == []) then [] 
              else curNode:search
      
    dijkstrasLoop:: [Node] -> [Node] -> Map -> [Node] -> Node -> [Node]
    dijkstrasLoop [] curSol _ _ _ = curSol
    dijkstrasLoop (x:xs) curSol map explored end = do
      let search = dijkstras x map explored end
      if search == [] then dijkstrasLoop xs curSol map explored end
      else if (length search) < (length curSol) || curSol == [] then dijkstrasLoop xs search map explored end
      else dijkstrasLoop xs curSol map explored end
        
    getPos :: Eq a => a -> [a] -> Int -> Int
    getPos a (x:xs) j 
      | x == a = j
      | otherwise = (getPos a xs (j+1))
      
    contains:: Eq a => a -> [a] -> Bool
    contains _ [] = False
    contains a (x:xs)
      | a == x = True
      | otherwise = contains a xs


    removeFrom:: Eq a => [a] -> [a] -> [a]
    removeFrom _ [] = []
    removeFrom [] b = b
    removeFrom (x:xs) from = removeFrom xs (remove x from)


    remove:: Eq a => a -> [a] ->[a]
    remove _ [] = []
    remove z (x:xs)
      | x == z = remove z xs
      | otherwise = x:(remove z xs)

    getPossibleLoc:: Int -> Map -> [Int]
    getPossibleLoc _ [] = []
    getPossibleLoc i (x:xs)
      | fst x == i = (snd x):(getPossibleLoc i xs)
      | snd x == i = (fst x):(getPossibleLoc i xs)
      | otherwise = (getPossibleLoc i xs)



solve :: Game -> Solution
solve = undefined

walkthrough :: IO ()
walkthrough = (putStrLn . unlines . filter (not . null) . map format . solve) start
  where
    format (Travel []) = ""
    format (Travel xs) = "Travel: " ++ unwords (map show xs)
    format (Select xs) = "Select: " ++ foldr1 (\x y -> x ++ ", " ++ y) xs
    format (Talk   []) = ""
    format (Talk   xs) = "Talk:   " ++ unwords (map show xs)


------------------------- Game data

start :: Game
start = Game theMap 0 [] theCharacters

theMap :: Map
theMap = [(1,2),(1,6),(2,4)]

theLocations :: [Location]
theLocations =
  -- Logicester
  [ "Home"           -- 0
  , "Brewpub"        -- 1
  , "Hotel"          -- 2
  , "Hotel room n+1" -- 3
  , "Temple"         -- 4
  , "Back of temple" -- 5
  , "Takeaway"       -- 6
  , "The I-50"       -- 7
  ]

theDescriptions :: [String]
theDescriptions =
  [ "your own home. It is very cosy."
  , "the `Non Tertium Non Datur' Brewpub & Barber's."
  , "the famous Logicester Hilbert Hotel & Resort."
  , "front of Room n+1 in the Hilbert Hotel & Resort. You knock."
  , "the Temple of Linearity, Logicester's most famous landmark, designed by Le Computier."
  , "the back yard of the temple. You see nothing but a giant pile of waste paper."
  , "Curry's Indian Takeaway, on the outskirts of Logicester."
  , "a car on the I-50 between Logicester and Computerborough. The road is blocked by a large, threatening mob."
  ]

theCharacters :: [Party]
theCharacters =
  [ ["Bertrand Russell"]                    -- 0  Home
  , ["Arend Heyting","Luitzen Brouwer"]     -- 1  Brewpub
  , ["David Hilbert"]                       -- 2  Hotel
  , ["William Howard"]                      -- 3  Hotel room n+1
  , ["Jean-Yves Girard"]                    -- 4  Temple
  , []                                      -- 5  Back of temple
  , ["Haskell Curry", "Jean-Louis Krivine"] -- 6  Curry's takeaway
  , ["Gottlob Frege"]                       -- 7  I-50
  ]

theDialogues :: [(Party,Dialogue)]
theDialogues = let
  always _ = True
  end str  = Choice str []
  isconn  _ _  Over           = False
  isconn  i j (Game m _ _ _ ) = elem i (connected m j)
  here         Over           = 0
  here        (Game _ n _ _ ) = n
  inParty   _  Over           = False
  inParty   c (Game _ _ p _ ) = elem c p
  isAt    _ _  Over           = False
  isAt    n c (Game _ _ _ ps) = elem c (ps !! n)
  updateMap _  Over           = Over
  updateMap f (Game m n p ps) = Game (f m) n p ps
 in
  [ ( ["Russell"] , Choice "Russell: Let's go on an adventure!"
      [ ("Sure." , end "You pack your bags and go with Russell.")
      , ("Maybe later.", end "Russell looks disappointed.")
      ]
    )
  , ( ["Heyting","Russell"] , end "Heyting: Hi Russell, what are you drinking?\nRussell: The strong stuff, as usual." )
  , ( ["Bertrand Russell"] , Branch (isAt 0 "Bertrand Russell") ( let
      intro = "A tall, slender, robed character approaches your home. When he gets closer, you recognise him as Bertrand Russell, an old friend you haven't seen in ages. You invite him in.\n\nRussell: I am here with a important message. The future of Excluded-Middle Earth hangs in the balance. The dark forces of the Imperator are stirring, and this time, they might not be contained.\n\nDo you recall the artefact you recovered in your quest in the forsaken land of Error? The Loop, the One Loop, the Loop of Power? It must be destroyed. I need you to bring together a team of our finest Logicians, to travel deep into Error and cast the Loop into lake Bottom. It is the only way to terminate it."
      re1   = ("What is the power of the Loop?" , Choice "Russell: for you, if you put it on, you become referentially transparent. For the Imperator, there is no end to its power. If he gets it in his possession, he will vanquish us all." [re2])
      re2   = ("Let's go!" , Action "Let's put our team together and head for Error." (updateMap (connect 1 0) . add ["Bertrand Russell"] . removeHere ["Bertrand Russell"]) )
      in Choice intro [re1,re2]
      ) ( Branch ( (==7).here) (end "Russell: Let me speak to him and Brouwer."
      ) (end "Russell: We should put our team together and head for Error." ) )
    )
  , ( ["Arend Heyting"] , Choice "Heyting: What can I get you?"
      [ ( "A pint of Ex Falso Quodbibet, please." , end "There you go." )
      , ( "The Hop Erat Demonstrandum, please."   , end "Excellent choice." )
      , ( "Could I get a Maltus Ponens?"          , end "Mind, that's a strong one." )
      ]
    )
  , ( ["Luitzen Brouwer"] , Branch (isAt 1 "Luitzen Brouwer")
      ( Choice "Brouwer: Haircut?"
        [ ( "Please." , let
          intro = "Brouwer is done and holds up the mirror. You notice that one hair is standing up straight."
          r1 i  = ( "There's just this one hair sticking up. Could you comb it flat, please?" , d i)
          r2    = ( "Thanks, it looks great." , end "Brouwer: You're welcome.")
          d  i  | i == 0    = Choice intro [r2]
                | otherwise = Choice intro [r1 (i-1),r2]
        in d 100)
        , ( "Actually, could you do a close shave?" , end "Of course. I shave everyone who doesn't shave themselves." )
        , ( "I'm really looking for help." , Choice "Brouwer: Hmmm. What with? Is it mysterious?"
          [ ( "Ooh yes, very. And dangerous." , Action "Brouwer: I'm in!" (add ["Luitzen Brouwer"] . removeHere ["Luitzen Brouwer"]) )
          ] )
        ]
      )
      ( end "Nothing" )
    )
  , ( ["David Hilbert"] , Branch (not . isconn 2 3) (let
        intro = "You wait your turn in the queue. The host, David Hilbert, puts up the first guest in Room 1, and points the way to the stairs.\n\nYou seem to hear that the next couple are also put up in Room 1. You decide you must have misheard. It is your turn next.\n\nHilbert: Lodging and breakfast? Room 1 is free."
        re1   = ("Didn't you put up the previous guests in Room 1, too?" , Choice "Hilbert: I did. But everyone will move up one room to make room for you if necessary. There is always room at the Hilbert Hotel & Resort." [("But what about the last room? Where do the guests in the last room go?" , Choice "Hilbert: There is no last room. There are always more rooms." [("How can there be infinite rooms? Is the hotel infinitely long?" , Choice "Hilbert: No, of course not! It was designed by the famous architect Zeno Hadid. Every next room is half the size of the previous." [re2])])])
        re2   =  ("Actually, I am looking for someone." , Action "Hilbert: Yes, someone is staying here. You'll find them in Room n+1. Through the doors over there, up the stairs, then left." (updateMap (connect 2 3)))
      in Choice intro [re1,re2]
      ) (end "Hilbert seems busy. You hear him muttering to himself: Problems, problems, nothing but problems. You decide he has enough on his plate and leave." )
    )
  , ( ["William Howard"] ,  Branch (isAt 3 "William Howard")
      (Choice "Howard: Yes? Are we moving up again?" [("Quick, we need your help. We need to travel to Error." , Action "Howard: Fine. My bags are packed anyway, and this room is tiny. Let's go!" (add ["William Howard"] . removeAt 3 ["William Howard"]))]
      ) (Branch (isAt 6 "William Howard") (Choice "Howard: What can I get you?"
        [ ("The Lambda Rogan Josh with the Raita Monad for starter, please." , end "Coming right up.")
        , ("The Vindaloop with NaN bread on the side." , Choice "Howard: It's quite spicy." [("I can handle it." , end "Excellent." ) ] )
        , ("The Chicken Booleani with a stack of poppadums, please.", end "Good choice." )
        ]
      ) (end "Howard: We need to find Curry. He'll know the way.")
    ) )
  , ( ["Jean-Yves Girard"] , Branch (isconn 4 5)  (end "You have seen enough here.") (Action "Raised on a large platform in the centre of the temple, Girard is preaching the Linearity Gospel. He seems in some sort of trance, so it is hard to make sense of, but you do pick up some interesting snippets. `Never Throw Anything Away' - you gather they must be environmentalists - `We Will Solve Church's Problems', `Only This Place Matters'... Perhaps, while he is speaking, now is a good time to take a peek behind the temple..." (updateMap (connect 4 5) ))
    )
  , ( ["Vending machine"] , Choice "The walls of the Temple of Linearity are lined with vending machines. Your curiosity gets the better of you, and you inspect one up close. It sells the following items:"
      [ ( "Broccoli"  , end "You don't like broccoli." )
      , ( "Mustard"   , end "It might go with the broccoli." )
      , ( "Watches"   , end "They seem to have a waterproof storage compartment. Strange." )
      , ( "Camels"    , end "You don't smoke, but if you did..." )
      , ( "Gauloises" , end "You don't smoke, but if you did..." )
      ]
    )
  , ( ["Jean-Louis Krivine"] , end "Looking through the open kitchen door, you see the chef doing the dishes. He is rinsing and stacking plates, but it's not a very quick job because he only has one stack. You also notice he never passes any plates to the front. On second thought, that makes sense - it's a takeaway, after all, and everything is packed in cardboard boxes. He seems very busy, so you decide to leave him alone."
    )
  , ( ["Haskell Curry"] , Branch (isAt 6 "Haskell Curry")
      (Choice "Curry: What can I get you?"
        [ ("The Lambda Rogan Josh with the Raita Monad for starter, please." , end "Coming right up.")
        , ("The Vindaloop with NaN bread on the side." , Choice "Curry: It's quite spicy." [("I can handle it." , end "Excellent." ) ] )
        , ("The Chicken Booleani with a stack of poppadums, please.", end "Good choice." )
        , ("Actually, I am looking for help getting to Error." , end "Curry: Hmm. I may be able to help, but I'll need to speak to William Howard.")
        ]
      ) (end "Nothing")
    )
  , ( ["Haskell Curry","William Howard"] , Branch (not . isconn 6 7) (Action "Curry:  You know the way to Error, right?\nHoward: I thought you did?\nCurry:  Not really. Do we go via Computerborough?\nHoward: Yes, I think so. Is that along the I-50?\nCurry:  Yes, third exit. Shall I go with them?\nHoward: sure. I can watch the shop while you're away." (add ["Haskell Curry"] . removeAt 6 ["Haskell Curry"] . addAt 6 ["William Howard"] . remove ["William Howard"] . updateMap (connect 6 7) )) (end "It's easy, just take the third exit on I-50.")
    )
  , ( ["Gottlob Frege"] , end "A person who appears to be the leader of the mob approaches your vehicle. When he gets closer, you recognise him as Gottlob Frege. You start backing away, and he starts yelling at you.\n\nFrege: Give us the Loop! We can control it! We can wield its power!\n\nYou don't see a way forward. Perhaps Russell has a plan." )
  , ( ["Bertrand Russell","Gottlob Frege","Luitzen Brouwer"] , let
        intro = "Frege is getting closer, yelling at you to hand over the Loop, with the mob on his heels, slowly surrounding you. The tension in the car is mounting. But Russell calmly steps out to confront Frege.\n\nRussell:"
        re1   = ( "You cannot control its power! Even the very wise cannot see all ends!" , Choice "Frege: I can and I will! The power is mine!\n\nRussell:" [re2,re3] )
        re2   = ( "Brouwer, whom do you shave?" , Choice "Brouwer: Those who do not shave themselves. Obviously. Why?\n\nRussell:" [re3] )
        re3   = ( "Frege, answer me this: DOES BROUWER SHAVE HIMSELF?" , Action
                  "Frege opens his mouth to shout a reply. But no sound passes his lips. His eyes open wide in a look of bewilderment. Then he looks at the ground, and starts walking in circles, muttering to himself and looking anxiously at Russell. The mob is temporarily distracted by the display, uncertain what is happening to their leader, but slowly enclosing both Frege and Russell. Out of the chaos, Russell shouts:\n\nDRIVE, YOU FOOLS!\n\nYou floor it, and with screeching tires you manage to circle around the mob. You have made it across.\n\nEND OF ACT 1. To be continued..."
                  (const Over)
                )
      in Choice intro [re1,re2,re3]
    )
  , ( ["Bertrand Russell","Haskell Curry","Luitzen Brouwer"] , Branch ((==7).here) (end "Road trip! Road trip! Road trip!") (end "Let's head for Error!")
    )
  ]