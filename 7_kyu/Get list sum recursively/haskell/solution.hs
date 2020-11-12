module SumRecursively where

sumR :: [Int] -> Int
sumR xs = foldr (+) 0 xs
