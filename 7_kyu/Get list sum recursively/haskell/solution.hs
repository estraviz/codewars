module SumRecursively where

sumR :: [Int] -> Int
sumR []     = 0
sumR (x:xs) = x + sumR xs
