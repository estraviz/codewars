-- SQL with LOTR: Elven Wildcards
-- PostgreSQL 9.6
SELECT
  INITCAP(CONCAT(firstname, ' ', lastname)) AS shortlist
FROM elves
WHERE
  firstname LIKE '%tegil%'
  OR lastname LIKE '%astar%'