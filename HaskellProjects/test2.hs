

count :: Int -> [Int]
count x = (countto 1 x)
    where
        countto :: Int -> Int -> [Int]
        countto n x
            | n>x =[]
            | otherwise = n:(countto (n+1) x)

foldleft :: (b -> a -> b) -> b -> [a] -> b
foldleft f u [] = u
foldleft f u (x:xs) = foldleft f (f u x) xs

add = foldleft (+) 0

times = foldleft (*) 1

size xs = foldleft f 0 xs
    where f a _ = a+1

concatenate = foldleft (++) []

reverseOnto ys [] = ys
reverseOnto ys (x:xs) = reverseOnto (x:ys) xs

revrs :: [a] -> [a]
revrs f = foldleft f []