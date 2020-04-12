-- Recursion #1 - Factorial: Create recursively the table with n up to and including 16
-- PostgreSQL 9.6
WITH RECURSIVE factorial (n, fact) AS (
  SELECT
    0,
    CAST(1 AS BIGINT)
  UNION ALL
  SELECT
    n + 1,
    (n + 1) * fact
  FROM factorial
)
SELECT
  n,
  fact
FROM factorial
LIMIT 17