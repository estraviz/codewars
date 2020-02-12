-- SQL Basics: Simple MIN / MAX
-- SQL - PostgreSQL 9.6
SELECT
  MIN(age) as age_min,
  MAX(age) as age_max
FROM people;