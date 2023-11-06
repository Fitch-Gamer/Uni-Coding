square::Int->Int
square x = x^2

tripCheck :: Int->Int->Int->Bool
tripCheck a b c = square c == square b + square a

factorial :: Int -> Int
factorial n
    | n <= 1 = 1
    | otherwise = factorial (n-1) * n

power :: Int->Int->Int
power a b
    | b<0 = error "Negative powers"
    | b==1 = a
    | otherwise = (power a (b-1)) * a

powerEbS :: Int->Int->Int
powerEbS a b
    | b<0 = error "Negative powers"
    | b==1 = a 
    | mod b 2 ==0 = (powerEbS (square a) (div b 2))
    | otherwise = (powerEbS (square a) (div (b-1) 2)) * a

euclid :: Int->Int->Int
euclid x y
    | x<0 || y<0 = error "negative inputs"
    | x==y = x
    | x<y = euclid x (y-x)
    | y<x = euclid y (x-y)

pow :: Int->Int->Int
pow a b =
    if b<0 then error "Negative powers" else
    if b==1 then a
    else (power a (b-1)) * a

powEbS :: Int->Int->Int
powEbS a b =
    if b<0 then error "Negative powers" else
    if b==1 then a else
    if mod b 2 == 0 then (powerEbS (square a) (div b 2))
    else (powerEbS (square a) (div (b-1) 2)) * a

collatz :: Int->Int
collatz a =
    if a == 1 then 1 else
    if (mod a 2) == 0 then collatz (div a 2)
    else collatz (3*a + 1)

collatzCount :: Int -> Int -> Int
collatzCount a b =
    if a == 1 then b else
    if (mod a 2) == 0 then collatzCount (div a 2) b+1
    else collatzCount (3*a + 1) b+1

collatzMax :: Int -> (Int,Int) -> (Int,Int)
collatzMax n (m,s)
    | n == 0 =(m,s)
    | (collatzCount n 0) > s = collatzMax (n-1) (n,(collatzCount n 0))
    | otherwise = collatzMax (n-1) (m,s)

ackermann :: Int -> Int -> Int
ackermann m n
    | m==0 = n+1
    | n==0 = ackermann (m-1) 1 
    | otherwise = ackermann (m-1) (ackermann m (n-1))


forLoopOne :: Int -> a -> (a -> IO b) -> IO b
forLoopOne i a f =
    if i==0 then f (a) 
    else 
    do f (a)
       forLoopOne (i-1) a f 

forLoopTwo :: Int -> a -> c -> (a -> c -> IO b) -> IO b
forLoopTwo i a c f =
    if i==0 then f a c 
    else 
    do f a c
       forLoopTwo (i-1) a c f 


testIo :: String -> IO()
testIo a = putStrLn a

testIoTwo :: String -> String -> IO()
testIoTwo a b = putStrLn (a++b)

times :: [Int] -> Int
times (x:xs)
    | xs == [] = x
    | otherwise = x* (times xs)

range :: Int->Int->[Int]
range n m = [n..m]

factorialTwo :: Int->Int
factorialTwo f = (times (range 1 f))

count :: Eq a => [a] -> Int
count [] = error "Empty list"
count (x:xs)
    | xs == [] = 1
    | otherwise = (count xs) + 1

append :: [a] -> [a] -> [a]
append a b = a++b

concatenate :: Eq a => [[a]] -> [a]
concatenate [] = error "Empty list"
concatenate (a:as)
    | as==[] = a
    | otherwise = (append a (concatenate as))

member :: Eq a => a-> [a]  -> Bool
member b [] = error "Empty list"
member b (a:as)
    | a == b = True
    | as == [] = False
    | otherwise = member b as

remove :: Eq a => a -> [a] -> [a]
remove a [] = error "Empty list"
remove a (b:bs) =
    if bs == [] then 
        if a == b then []
        else [b]
    else
        if a == b then remove a bs
        else [b] ++ remove a bs

at :: Eq a => [a] -> Int -> a
at [] i = error "Empty list"
at (x:xs) i
    | i<0 = error "Negative index"
    | i == 0 = x
    | xs == [] = error "Index too large"
    | otherwise = at xs (i-1)

final :: Eq a=>[a] -> a
final [] = error "Empty list"
final (x:xs)
    | xs == [] = x
    | otherwise = final xs

ordered :: [Int] -> Bool
ordered [] = error "Empty list"
ordered (x:xs:xss)
    | xs < x = False
    | xss == [] = True
    | otherwise = ordered ([xs]++xss)

pair :: Eq a => [a] -> Eq b => [b] -> [(a,b)]
pair [] [] = error "Empty list"
pair (a:as) (x:xs)
    | (as==[]) || (xs==[]) = [(a,x)]
    | otherwise = [(a,x)] ++ pair as xs

find :: Int -> [(Int,String)] -> String
find i [] = error "Empty list"
find i (x:xs)
    | xs == [] = ""
    | i == fst x = snd x
    | otherwise = find i xs

merge :: [Int] -> [Int] -> [Int]
merge [] [] = error "Empty list"
merge (x:xs) (z:zs) =
    if xs == [] && x <= z then [x] ++ (z:zs)
    else if zs == [] && z <= x then [z] ++ (x:xs)
    else if x <=z then [x] ++ merge xs (z:zs)
    else [z] ++ merge (x:xs) zs

msort :: [Int] ->[Int]
msort [] = error "Empty list"
msort (x:xs) = head (mSorting (oneElement (x:xs)))

mSorting:: [[Int]] -> [[Int]]
mSorting [] = error "Empty list"
mSorting (x:xs) =
    let y = (mSortOne (x:xs))
    in if length y == 1 then y else mSorting y

mSortOne :: [[Int]] -> [[Int]]
mSortOne [] = error "Empty list"
mSortOne (x:xs)
    | xs == [] = [x]
    | head xs == [] = [x]
    | tail xs == [] = [merge x (head xs)]
    | otherwise = [(merge x (head xs))] ++ mSortOne (tail xs) 


oneElement :: Eq a =>[a] ->[[a]]
oneElement [] = error "Empty list"
oneElement (x:xs)
    | xs == [] = [[x]]
    | otherwise = [[x]] ++ oneElement xs

squareSum :: Int -> Int -> (Int -> Int) ->Int
squareSum x y f  = (f x) + (f y)

indivisible:: Int -> Int -> Bool
indivisible x y
    | x == y = False
    | otherwise = mod x y == 0

primeFilter :: [Int] -> [Int]
primeFilter (x:xs) = prFilter 2 (x:xs)

prFilter :: Int -> [Int] -> [Int]
prFilter x (y:ys)
    | x >=(maximum (y:ys))= (y:ys)
    | otherwise = prFilter (x+1) (filter (indivisible x) (y:ys))

doubles :: [Int]->[Int]
doubles (x:xs)
    | xs == [] = [2*x]
    | otherwise = [2*x] ++ doubles xs

doublesMap :: [Int]->[Int]
doublesMap (x:xs) = map (2*) (x:xs)

multiplesOfThree :: [Int] -> [Int]
multiplesOfThree (x:xs) = filter (modThree) (x:xs)
    where 
        modThree x = (mod x 3) == 0


doubleMultiplesOfThree :: [Int] -> [Int]
doubleMultiplesOfThree (x:xs) = doublesMap (multiplesOfThree (x:xs))

shorts :: [String] -> [String]
shorts (x:xs) = filter (short) (x:xs)
    where
        short x = (length x) <= 4

incrementPositives :: [Int] ->[Int]
incrementPositives (x:xs) = map addPositives (x:xs)
    where
        addPositives x = if mod x 2 == 0 then x+1 else x

difference :: String -> String ->String
difference (x:xs) (y:ys)
    | ys == [] = filter (y /=) (x:xs)
    | otherwise = difference (filter (y /=) (x:xs)) ys

oddLengthSums :: [[Int]] -> [Int]
oddLengthSums (x:xs) = map sum (filter (oddLength) (x:xs))
    where
        oddLength x = mod (length x) 2 /= 0

numbered :: [a] -> [(Int,a)]
numbered (x:xs) = zip [1..] (x:xs)

everyother :: Eq a => [a] -> [a]
everyother (x:xs) = delOther (x:xs) 1
    where
        delOther :: Eq a => [a] -> Int -> [a]
        delOther (y:ys) b 
            | ys == [] = if mod b 2 == 0 then [] else [y]
            | mod b 2 == 0 = delOther ys (b+1)
            | otherwise = [y] ++ delOther ys (b+1)

same :: Eq a => [a] -> [a] -> [Int]
same (x:xs) (y:ys) = compSame (x:xs) (y:ys) 1
    where
        compSame :: Eq a => [a] -> [a] -> Int -> [Int]
        compSame (x:xs) (y:ys) a
            | xs == [] || ys == [] = if x==y then [a] else []
            | x == y = [a] ++ compSame xs ys (a+1)
            | otherwise = compSame xs ys (a+1)

myMap :: [a] -> (a -> a) -> [a]
myMap [] f = []
myMap (x:xs) f = [f x] ++ myMap xs f


data Fraction = Fraction Integer Integer 

fraction :: Integer -> Integer -> Fraction
fraction n d
    | d == 0 = error "Cannot have 0 denomenator"
    | d < 0 = Fraction (div(-n) x) (div (-d) x)
    | otherwise = Fraction(div n x) (div d x)
    where x = gcd n d