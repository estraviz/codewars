-- # write your SQL statement here:
-- you are given a table 'ispalindrome' with column 'str',
-- return a table with column 'str' and your result in a column named 'res'.
-- The result should be 'True' if the string is a palindrome, and 'False' if it is not.
-- PostgeSQL 13.0
SELECT str AS str,
    CASE
        WHEN LOWER(str) = LOWER(REVERSE(str)) THEN True
        ELSE False
    END AS res
FROM ispalindrome