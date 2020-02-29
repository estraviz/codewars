-- SQL Basics: Simple GROUP BY
-- PostgreSQL 9.6
SELECT
  age,
  count(*) as people_count
FROM people
GROUP BY
  age