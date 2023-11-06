

------------------------- Exercise 1

doubles :: [Int] -> [Int]
doubles (x:xs) = [2*n| n<-(x:xs)]

multiplesOfThree :: [Int] -> [Int]
multiplesOfThree (x:xs) = [n|n<-(x:xs), (mod n 3)==0]

doubleMultiplesOfThree :: [Int] -> [Int]
doubleMultiplesOfThree (x:xs) = [2*n|n<-(x:xs), (mod n 3)==0]

shorts :: [[a]] -> [[a]]
shorts (x:xs) =[n|n<-(x:xs),(length n)<=3] 

incrementPositives :: (Ord a,Num a) => [a] -> [a]
incrementPositives (x:xs) = [n+1| n<-(x:xs),n>0]

difference :: Eq a => [a] -> [a] -> [a]
difference (x:xs) (y:ys) = [n| n<-(x:xs),b<-[h| h<-(y:ys)], b/= n]

oddLengthSums :: Num a => [[a]] -> [a]
oddLengthSums (x:xs) = [n|y<-(x:xs),n <- [sum y],(mod (length y) 2) == 1 ]

everyother :: [a] -> [a]
everyother (x:xs) = [n|b<-zip (x:xs) [1..],mod (snd b) 2 == 1 , n<- [fst b]]

same :: Eq a => [a] -> [a] -> [Int]
same (x:xs) (y:ys) = [n| b<-zip [1..] (zip (x:xs) (y:ys)),n<-[fst b], fst (snd b) == snd (snd b)]


------------------------- Exercise 2

combinations :: [a] -> [b] -> [(a,b)]
combinations (x:xs) (y:ys) = [n|q<-[h|h<-(x:xs)],w<-[b|b<-(y:ys)],n<-[(q,w)]] 

selfcombinations :: [a] -> [(a,a)]
selfcombinations (x:xs) = [n|q<- zip (x:xs) [1..],v<- zip (x:xs) [1..],n<- [(fst q,fst v)] , snd q <= snd v] 

pyts :: Int -> [(Int,Int,Int)]
pyts v = [n| x<- [1..v],y<- [1..v],z<- [1..v], x^2 + y^2 == z^2, y>x, n<- [(x,y,z)]]


------------------------- Exercise 3

allTrue :: [Bool] -> Bool
allTrue (x:xs) = foldr1 (&&) (x:xs)

someTrue :: [Bool] -> Bool
someTrue (x:xs) = foldr1 (||) (x:xs)

largest :: Ord a => [a] -> a
largest (x:xs) = foldr1 (larger) (x:xs)
    where
        larger:: Ord b => b->b->b
        larger q w
            | q>w = q
            | otherwise = w

smallest :: Ord a => [a] -> a
smallest (x:xs) = foldr1 (smaller) (x:xs)
    where
        smaller:: Ord b => b->b->b
        smaller q w
            | q<w = q
            | otherwise = w

every :: (a -> Bool) -> [a] -> Bool
every f (x:xs) = foldr ((&&).f) (True) (x:xs) 

some :: (a -> Bool) -> [a] -> Bool
some f (x:xs) = foldr ((||).f) (False) (x:xs) 

select :: (a -> Bool) -> [a] -> [a]
select p = foldr f []
    where f x xs | p x  = x:xs
                 | otherwise = xs 

------------------------- Exercise 4

evenLength :: String -> Bool
evenLength (x:xs) = foldr (nand) True (map (makeTrue) (x:xs))
    where
        makeTrue :: a -> Bool
        makeTrue a = True

        nand :: Bool -> Bool -> Bool
        nand a b 
            | a == b = False
            | otherwise = True

count :: Char -> String -> Int
count a (x:xs) = sum (map(comp a) (x:xs))
    where
        comp :: Char -> Char -> Int
        comp a b = if a==b then 1 else 0

successive :: Char -> String -> Int
successive = undefined


------------------------- Exercise 5

selections :: [a] -> [[a]]
selections [] = [[]]
selections (x:xs) = [x:ys| ys<-yss]  ++ yss
    where
        yss = selections xs

splits :: [a] -> [([a],[a])]
splits = undefined

permutations :: [a] -> [[a]]
permutations a = undefined
 