-- SQL Basics: Up and Down
-- PostgreSQL 9.6
SELECT
  CASE
    WHEN SUM(number1) % 2 = 1 THEN MIN(number1)
    ELSE MAX(number1)
  END AS number1,
  CASE
    WHEN SUM(number2) % 2 = 1 THEN MIN(number2)
    ELSE MAX(number2)
  END AS number2
FROM numbers