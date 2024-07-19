times:: [Int] -> Int
times xs = multiply 1 xs
where
    multiply result [] = result
    multiply result (x:xs) = multiply (result * x) xs