-- SQL: Concatenating Columns
-- PostreSQL 9.6
SELECT
  CONCAT(prefix, ' ', first, ' ', last, ' ', suffix) AS title
FROM names