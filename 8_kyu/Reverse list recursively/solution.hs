module ReverseRecursively where

revR :: [Int] -> [Int]
revR [] = []
revR (x:xs) = revR xs ++ [x]
