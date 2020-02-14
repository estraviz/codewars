-- SQL: Right and Left
-- PostgreSQL 9.6
SELECT
  LEFT(project, commits) as project,
  RIGHT(address, contributors) as address
FROM repositories;