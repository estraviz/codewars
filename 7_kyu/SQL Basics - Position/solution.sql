-- SQL Basics - Position
-- PostgreSQL 9.6
SELECT
  id,
  name,
  POSITION(',' IN characteristics) AS comma
FROM monsters
ORDER BY comma