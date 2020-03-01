-- SQL Basics: Repeat and Reverse
-- PostgreSQL 9.6
SELECT
  REPEAT(name, 3) as name,
  REVERSE(characteristics) AS characteristics
FROM monsters